#encoding=utf-8
#from tornado
import os.path
import re
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
from tornado.options import define, options
#from openyoudao
import webshot
import thread
import webkit, gtk
from time import sleep
import gl 
import os
import sys
import fusionyoudao
#from record_xclip 
# Change path so we find Xlib
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Xlib import X, XK, display
from Xlib.ext import record
from Xlib.protocol import rq
record_dpy = display.Display()
ctx = record_dpy.record_create_context(
0,
[record.AllClients],
[{
'core_requests': (0, 0),
'core_replies': (0, 0),
'ext_requests': (0, 0, 0, 0),
'ext_replies': (0, 0, 0, 0),
'delivered_events': (0, 0),
'device_events': (X.KeyPress, X.MotionNotify),
'errors': (0, 0),
'client_started': False,
'client_died': False,
}])

define("port", default=8888, help="run on the given port", type=int)
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
             (r"/", HomeHandler),
             (r"/index", IndexHandler),
             (r"/search", SearchHandler),
             (r"/dictscreen", DictScreenHandler),
        ]
        settings = dict(
            urlcheck_title=u"URL",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            ) 
        tornado.web.Application.__init__(self, handlers, **settings)
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db
class HomeHandler(BaseHandler):
    def get(self):
	info="Openyoudao"
        self.render("youdao/start.html",info=info) 
class IndexHandler(BaseHandler):
    def get(self):
        global flush
        flush=0
	record_dpy.record_disable_context(ctx)
	info="Openyoudao"
        self.render("youdao/start.html",info=info) 
class SearchHandler(BaseHandler):
    def post(self):
	keyword=self.get_argument('keyword')
	print keyword
	fusion(keyword)
        self.render("public/result.html",) 
class DictScreenHandler(BaseHandler):
    def get(self):
	print "dicscreen hahahahahah"
	#self.render("youdao/quci.html",)
	self.render("public/result.html",)
        global flush
        global change
        global Alive
        flush=1
	while flush and Alive:
	    print "进入循环"
            if change==1:	
	        print "开始加载"
		self.flush
                #self.render("public/result.html",) 
                #self.render("youdao/start.html",) 
		self.finish
		change=0
            sleep(1)
	#gettext()
	
def gettext():
    os.system("xclip -f /dev/null")           #清空剪切板
    record_dpy.record_enable_context(ctx,record_callback)
    record_dpy.record_free_context(ctx)
def fusion(keyword):
    url= "http://dict.youdao.com/search?q=" + keyword
    print url
    origindir="templates/public/origin.html";
    os.system("curl -s -w %{http_code}:%{time_connect}:%{time_starttransfer}:%{time_total}:%{speed_download} -o \'" + origindir +"\' \'" + url+ "\'")
    fusionyoudao.reconstruct()
def tornado_init():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
def record_callback(reply):
    if reply.category != record.FromServer:
        return
    if reply.client_swapped:
        print "* received swapped protocol data, cowardly ignored"
        return
    if not len(reply.data) or ord(reply.data[0]) < 2:
    # not an event
        return
    data = reply.data
    while len(data):
        event, data = rq.EventField(None).parse_binary_value(data, record_dpy.display, None, None)   
   	if event.type == X.ButtonRelease:
            # get text
            pipe = os.popen("xclip -o")
            text = pipe.readline()
            pipe.readlines()    #清空管道剩余部分
            pipe.close()
            print "您选取的是: ", text
	    global pre_text
	    global change
            text = text.strip('\r\n\x00').lower()
            if(pre_text != text and text!=""):
		pre_text = text
		if flush ==1: 
	            fusion(text)
		    change=1
def webshow():
    global window
    global Alive
    window = webshot.Window()
    window.load("http://127.0.0.1:8888")
    window.show()
    gtk.main()
    Alive=0
def main():
    global Alive
    global flush
    global change
    global pre_text
    Alive=1
    flush=1
    change=0
    pre_text = ""
    thread.start_new_thread(tornado_init,())
    sleep(1)
    thread.start_new_thread(webshow,())
    sleep(1)
    thread.start_new_thread(gettext,())
    while Alive:
        sleep(0.5)
if __name__ == "__main__":
    main()
