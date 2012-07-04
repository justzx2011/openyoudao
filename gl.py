import os
import sys
import sqlite3
global keywordtext
global proxyDict
global downloadwait
global baseurl
global lock
global prebaseurl
global homedir
global datadir
global historydir
global origindir
global resultdir
global url
global homeurl
global headyoudao
global bodystartyoudao
global bodystarticb
global bodyendicb
global headicb
proxyDict = {}  #默认不设置代理
"""
# SOCKS5 proxy for HTTP/HTTPS
proxyDict = {
    'http' : "socks5://1.2.3.4:1080",
    'https' : "socks5://1.2.3.4:1080"
}

# SOCKS4 proxy for HTTP/HTTPS
proxyDict = {
    'http' : "socks4://1.2.3.4:1080",
    'https' : "socks4://1.2.3.4:1080"
}

# HTTP proxy for HTTP/HTTPS
proxyDict = {
    'http' : "1.2.3.4:1080",
    'https' : "1.2.3.4:1080"
}
"""
keywordtext = ""
baseurl=""
lock=0
userdir=os.path.expanduser('~')
datadir=userdir + "/.local/share/webkit/databases/file__0.localstorage"
sqlitedir=userdir + "/.local/share/webkit"
prebaseurl=""
url=""
workdir = os.getcwd()
homedir = sys.path[0]
youdaosqlitedir = homedir + "/cache/databases"
historydir = homedir + "/cache/history.cache"
origindir = homedir + "/cache/origin.html"
resultdir = homedir + "/cache/result.html"
headyoudao = homedir + "/cache/construction/youdao/head.html"
headicb = homedir + "/cache/construction/icb/head.html"
bodystartyoudao = homedir + "/cache/construction/youdao/body-start.txt"
bodystarticb = homedir + "/cache/construction/icb/body-start.txt"
bodyendicb = homedir + "/cache/construction/icb/body-end.txt"
homeurl = "file://" + homedir + "/cache/config.html"
baseurlyoudao="http://dict.youdao.com/search?q="
baseurlicb="http://www.iciba.com/"
downloadwait = "<html><body><b style=\"font-size:80px;position:absolute;top:42%;left:35%;\" >Wai    ting...</b></body></html>"
