import os
import sqlite3
global keywordtext
global baseurl
global lock
global prebaseurl
global homedir
global datadir
global url
keywordtext = ""
baseurl=""
lock=0
datadir=os.path.expanduser('~') + "/.local/share/webkit/databases/file__0.localstorage"
prebaseurl=""
url=""
homedir = os.getcwd()
baseurlyoudao="http://dict.youdao.com/search?q="
baseurlicb="http://www.iciba.com/"
