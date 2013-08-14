from BeautifulSoup import BeautifulSoup
import os
import gl
import re
import popen2
def reconstruct():
    print "start fusionyoudao"
    soup = BeautifulSoup(open("templates/origin.html"))
    head=open(gl.headyoudao,'r')
    bodystart=open(gl.bodystartyoudao,'r')
    #bodyend=open('cache/construction/youdao/body-end.txt','r')
    result = soup.find('div',{"id":"results"})
    #sousuo = soup.find('form',{"id":"f"})
    #sousuo  = str(sousuo).replace("action=\"/search\"","action=\"http://dict.youdao.com/search\"")
    #result  = str(result).replace("href=\"/example/","href=\"http://dict.youdao.com/example/")
    #os.system("echo "" > cache/result.html")
    f_tar=open(gl.resultdir,'w+')
    print >> f_tar,"<html>"
    print >> f_tar,head.read()
    print >> f_tar,"<body>"
    print >> f_tar,bodystart.read()
    #print >> f_tar,"\n"
    #print >> f_tar,"<div class=\"c-header\">"
    #print >> f_tar,sousuo
    #print >> f_tar,"</div>"
    print >> f_tar,result
    #print >> f_tar,bodyend.read()
    print >> f_tar,"</body></html>"
    f_tar.close()
    head.close()
    bodystart.close()
    #bodyend.close()
    os.system("sed -i -e 's/action=\"\/search/action=\"http:\/\/dict.youdao.com\/search/g' \'"+ gl.resultdir + "\'")
    os.system("sed -i -e 's/href=\"\/example/href=\"http:\/\/dict.youdao.com\/example/g' \'"+ gl.resultdir + "\'")
    print "fusionyoudao completed"
    #os.system("sed -i -e 's/<\/div><\/div><\/div>/ /g' cache/result.html")
