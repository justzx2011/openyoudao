from BeautifulSoup import BeautifulSoup
import os
import re
import popen2
def reconstruct():
    print "start fusionicb"
    homedir = os.getcwd()
    soup = BeautifulSoup(open(homedir +  "/cache/icb.html"))
    head=open('cache/construction/icb/head.html','r') 
    bodystart=open('cache/construction/icb/body-start.txt','r') 
    bodyend=open('cache/construction/icb/body-end.txt','r') 
    result = soup.find('div',{"id":"main_box"})
    sousuo = soup.find('div',{"class":"search_box"})
    f_tar=open('cache/result.html','w+')
    print >> f_tar,"<html>"
    print >> f_tar,head.read()
    print >> f_tar,"<body>"
    print >> f_tar,bodystart.read()
    print >> f_tar,"\n"
    print >> f_tar,"<div class=\"c-header\">"
    print >> f_tar,sousuo
    print >> f_tar,"</div>"
    print >> f_tar,result
    print >> f_tar,bodyend.read()
    print >> f_tar,"</body></html>"
    f_tar.close()
    head.close()
    bodystart.close()
    bodyend.close()
    #os.system("sed -i -e 's/action=\"\/search/action=\"http:\/\/dict.youdao.com\/search/g' cache/result.html")
    #os.system("sed -i -e 's/href=\"\/example/href=\"http:\/\/dict.youdao.com\/example/g' cache/result.html")
    #os.system("sed -i -e 's/<\/div><\/div><\/div>/ /g' cache/result.html")
    print "fusionicb completed"
