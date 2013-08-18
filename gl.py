#encoding=utf-8
import os
import sys
global downloadwait
global pre_text
global homedir
global origindir
global resultdir
global homeurl
global headyoudao
global bodystartyoudao

pre_text=""
userdir=os.path.expanduser('~')
cachedir = userdir + "/.openyoudao"
subcachedir = userdir + "/.openyoudao/cache"
workdir = os.getcwd()
homedir = sys.path[0]
origindir = cachedir + "/cache/origin.html"
resultdir = cachedir + "/cache/result.html"
headyoudao = "/var/cache/openyoudao/construction/youdao/head.html"
bodystartyoudao = "/var/cache/openyoudao/construction/youdao/body-start.txt"
homeurl = "file://" + "/var/cache/openyoudao/config.html"
baseurlyoudao="http://dict.youdao.com/search?q="
downloadwait = "<html><body><b style=\"font-size:80px;position:absolute;top:42%;left:35%;\" >Wai    ting...</b></body></html>"
