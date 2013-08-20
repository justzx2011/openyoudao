#encoding=utf-8
import os
import sys
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
headyoudao = "/usr/share/openyoudao/construction/youdao/head.html"
bodystartyoudao = "/usr/share/openyoudao/construction/youdao/body-start.txt"
homeurl = "file://" + "/usr/share/openyoudao/config.html"
baseurlyoudao="http://dict.youdao.com/search?q="
