#encoding=utf-8
import os
import sys
global pre_text
global cachedir
global homedir
global origindir
global resultdir
global homeurl
global headyoudao
global bodystartyoudao

pre_text=""
userdir=os.path.expanduser('~')
workdir = os.getcwd()
homedir = sys.path[0]
userdir=os.path.expanduser('~')
cachedir = userdir + "/.openyoudao"
origindir = userdir + "/.openyoudao/origin.html"
resultdir = userdir + "/.openyoudao/result.html"
headyoudao = "/usr/share/openyoudao/construction/youdao/head.html"
bodystartyoudao = "/usr/share/openyoudao/construction/youdao/body-start.txt"
homeurl = "file://" + "/usr/share/openyoudao/config.html"
baseurlyoudao="http://dict.youdao.com/search?q="
searchurl="http://dict.youdao.com/search?le=eng&q="
zh2en=searchurl
zh2jap="http://dict.youdao.com/search?le=jap&q="
zh2ko="http://dict.youdao.com/search?le=ko&q="
zh2fr="http://dict.youdao.com/search?le=ko&q="
