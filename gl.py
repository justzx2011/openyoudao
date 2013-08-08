#encoding=utf-8
import os
import sys
global downloadwait
global pre_text
global homedir
global datadir
global origindir
global resultdir
global url
global homeurl
global headyoudao
global bodystartyoudao
global bodystarticb
global bodyendicb
global headicb

pre_text=""
userdir=os.path.expanduser('~')
cachedir = userdir + "/.openyoudao"
subcachedir = userdir + "/.openyoudao/cache"
cachedirhistory = userdir + "/.openyoudao/cache/history.cache"
cachedirorigin = userdir + "/.openyoudao/cache/origin.html"
cachedirresult = userdir + "/.openyoudao/cache/result.html"
url=""
workdir = os.getcwd()
homedir = sys.path[0]
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
