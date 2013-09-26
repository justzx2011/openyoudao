#encoding=utf-8
import os.path
import os
import re
import torndb
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
from tornado.options import define, options
define("port", default=8081, help="run on the given port", type=int)
define("mysql_host", default="localhost:3306", help="database host")
define("mysql_database", default="blog", help="database name")
define("mysql_user", default="root", help="database user")
define("mysql_password", default="", help="database password")
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
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password) 
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db
class HomeHandler(BaseHandler):
    def get(self):
	info="blog"
        self.render("index.html",info=info) 
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port,address='108.174.49.132')
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
