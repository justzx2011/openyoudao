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
define("mysql_user", default="blog@youdao", help="database user")
define("mysql_password", default="youdao@163", help="database password")
