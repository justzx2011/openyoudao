#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import os
import gl
import re
import popen2
def reconstruct():
    print "start fusionyoudao"
    soup = BeautifulSoup(open(gl.origindir))
    head=open(gl.headyoudao,'r')
    result = soup.find('div',{"id":"results"})
    #sousuo = soup.find('form',{"id":"f"})
    #sousuo  = str(sousuo).replace("action=\"/search\"","action=\"http://dict.youdao.com/search\"")
    #result  = str(result).replace("href=\"/example/","href=\"http://dict.youdao.com/example/")
    #os.system("echo "" > cache/result.html")
    f_tar=open(gl.resultdir,'w+')
    print >> f_tar,"<html>"
    print >> f_tar,head.read()
    print >> f_tar,"<body>"
    #print >> f_tar,"\n"
    #print >> f_tar,"<div class=\"c-header\">"
    #print >> f_tar,sousuo
    #print >> f_tar,"</div>"
    print >> f_tar,result
    print >> f_tar,"</body></html>"
    f_tar.close()
    head.close()
    os.system("sed -i -e 's/action=\"\/search/action=\"http:\/\/dict.youdao.com\/search/g' \'"+ gl.resultdir + "\'")
    os.system("sed -i -e 's/href=\"\/example/href=\"http:\/\/dict.youdao.com\/example/g' \'"+ gl.resultdir + "\'")
    os.system("sed -i -e 's/href=\"\/simplayer.swf/href=\"http:\/\/dict.youdao.com\/simplayer.swf/g' \'"+ gl.resultdir + "\'")
    #os.system("sed -i -e 's/href=\"\/simplayer.swf/href=\"http:\/\/dict.youdao.com\/simplayer.swf/g' \'"+ gl.resultdir + "\'")
    os.system("sed -i -e 's/<h3>目录<\/h3>/<h3>%index<\/h3>/g' \'"+ gl.resultdir + "\'")
    os.system("sed -i -e 's/详细内容//g' \'"+ gl.resultdir + "\'")
    os.system("sed -i -e 's/更多双语例句//g' \'"+ gl.resultdir + "\'")
    os.system("sed -i -e 's/更多原声例句//g' \'"+ gl.resultdir + "\'")
    os.system("sed -i -e 's/更多权威例句//g' \'"+ gl.resultdir + "\'")
    os.system("sed -i -e '/onmousedown/'d \'"+ gl.resultdir + "\'")
    os.system("sed -i -e '/百度百科/'d \'"+ gl.resultdir + "\'")
    os.system("sed -i -e 's/<li class=\"nav-collins\"><a href=\"http:\/\/dict.youdao.com\/writing\/?keyfrom=dictweb\" hidefocus=\"true\">英文写作助手<\/a><span class=\"collins-icon\"><\/span><\/li>//g' \'"+ gl.resultdir + "\'")
    #os.system("sed -i -e 's/http:\/\/dict.youdao.com\/writing\/?keyfrom=dictweb/file:\/\/\/usr\/share\/openyoudao\/config.html/g' \'"+ gl.resultdir + "\'")
    print "fusionyoudao completed"
    #os.system("sed -i -e 's/<\/div><\/div><\/div>/ /g' cache/result.html")
