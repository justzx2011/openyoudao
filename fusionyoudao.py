from BeautifulSoup import BeautifulSoup
import os
import logging
import gl
import re
import popen2
def reconstruct():
    logging.info("start fusionyoudao")
    soup = BeautifulSoup(open(gl.origindir))
    head=open(gl.headyoudao,'r')
    result = soup.find('div',{"id":"results"})
    f_tar=open(gl.resultdir,'w+')
    print >> f_tar,"<html>"
    print >> f_tar,head.read()
    print >> f_tar,"<body>"
    print >> f_tar,result
    print >> f_tar,"</body></html>"
    f_tar.close()
    head.close()
    os.system("sed -i -e 's/action=\"\/search/action=\"http:\/\/dict.youdao.com\/search/g' \'"+ gl.resultdir + "\'")
    os.system("sed -i -e 's/href=\"\/example/href=\"http:\/\/dict.youdao.com\/example/g' \'"+ gl.resultdir + "\'")
    logging.info("fusionyoudao completed")
