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
import fusionyoudao
define("port", default=8888, help="run on the given port", type=int)
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
             (r"/", HomeHandler),
             (r"/search", SearchHandler),
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
        self.render("start.html",info=info) 
class SearchHandler(BaseHandler):
    def post(self):
        print "hahaha"
	keyword=self.get_argument('keyword')
        url= "http://dict.youdao.com/search?q=" + keyword
        print url
        os.system("curl -s -w %{http_code}:%{time_connect}:%{time_starttransfer}:%{time_total}:%{speed_download} -o \'" + gl.origindir +"\' \'" + url+ "\'")
        fusionyoudao.reconstruct()
        self.render("result.html",) 
        #gl.homeurl="file://" + gl.resultdir
        #window.load(gl.homeurl)
        #window.show()  
def tornado_init():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

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
    Alive=1
    thread.start_new_thread(tornado_init,())
    sleep(1)
    thread.start_new_thread(webshow,())
    while Alive:
        sleep(0.5)
if __name__ == "__main__":
    main()
