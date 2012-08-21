#encoding=utf-8
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
proxyDict = {} 

"""代理配置"""
## SOCKS5 proxy for HTTP/HTTPS
#proxyDict = {
#    'http' : "socks5://1.2.3.4:1080",
#    'https' : "socks5://1.2.3.4:1080"
#}
#
## SOCKS4 proxy for HTTP/HTTPS
#proxyDict = {
#    'http' : "socks4://1.2.3.4:1080",
#    'https' : "socks4://1.2.3.4:1080"
#}
#
## HTTP proxy for HTTP/HTTPS
#proxyDict = {
#    'http' : "1.2.3.4:1080",
#    'https' : "1.2.3.4:1080"
#}

keywordtext = ""
baseurl=""
lock=0
userdir=os.path.expanduser('~')
cachedir = userdir + "/.openyoudao"
datadir=userdir + "/.local/share/webkit/databases/file__0.localstorage"
sqlitedir=userdir + "/.local/share/webkit"
prebaseurl=""
url=""
workdir = os.getcwd()
homedir = sys.path[0]
youdaosqlitedir = "/var/cache/openyoudao/databases"
historydir = cachedir + "/cache/history.cache"
origindir = cachedir + "/cache/origin.html"
resultdir = cachedir + "/cache/result.html"
headyoudao = "/var/cache/openyoudao/construction/youdao/head.html"
headicb = "/var/cache/openyoudao/construction/icb/head.html"
bodystartyoudao = "/var/cache/openyoudao/construction/youdao/body-start.txt"
bodystarticb = "/var/cache/openyoudao/construction/icb/body-start.txt"
bodyendicb = "/var/cache/openyoudao/construction/icb/body-end.txt"
homeurl = "file://" + "/var/cache/openyoudao/config.html"
baseurlyoudao="http://dict.youdao.com/search?q="
baseurlicb="http://www.iciba.com/"
downloadwait = "<html><body><b style=\"font-size:80px;position:absolute;top:42%;left:35%;\" >Wai    ting...</b></body></html>"
