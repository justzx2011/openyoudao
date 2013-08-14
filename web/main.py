#encoding=utf-8
import os.path
import re
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
             (r"/", HomeHandler),
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
        self.render("index.html",info=info) 
     
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
