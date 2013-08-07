#encoding=utf-8 
from lxml import html
import popen2
import gl
import string
import sys
import webkit, gtk
import thread
import fusionyoudao
import fusionicb
import webshot
import record_xclip
import random
import os
from time import sleep
def lookup():
    pre_text=""
    text=""
    cmd = "tail -f " + gl.historydir 
    if(gl.baseurl==""):
        gl.baseurl=gl.baseurlyoudao
    myfile=os.popen(cmd)
    while True:
        text=myfile.readline().strip('\r\n\x00')
        if (pre_text != text or gl.prebaseurl != gl.baseurl) and text != "" : 
            pre_text = text
            print gl.lock
            gl.prebaseurl =  gl.baseurl
            url= gl.baseurl + text                           #合成地址
            os.system("curl -s -o \'" + gl.origindir +"\' \'" + url+ "\'") 	 #获得网页(非代理)
            fusionyoudao.reconstruct()                   #区分聚合
            gl.homeurl="file://" + gl.resultdir #合成最终缓冲访问地址
            window.load(gl.homeurl)                             #加载最终缓冲内容到浏览器
            window.show()                                    #显示结果
            gl.lock=0

def webshow():
    global window
    global Alive
    window = webshot.Window()
    window.load(gl.homeurl)
    window.show() 
    gtk.main() 
    Alive=0

def gettext():
    os.system("xclip -f /dev/null")           #清空剪切板
    os.system("/bin/echo "" > \'"+ gl.historydir + "\'")
    record_xclip.record_dpy.record_enable_context(record_xclip.ctx, record_xclip.record_callback)            
    record_xclip.record_dpy.record_free_context(record_xclip.ctx)

# Main thread
def main():
    
    #运行标志结束 
    global Alive
    Alive=1
    thread.start_new_thread(webshow,())
    sleep(1)
    thread.start_new_thread(gettext,())
    sleep(1)
    thread.start_new_thread(lookup,())
    	
    while Alive:
        sleep(1)
        

    print 'All threads have terminated.'
if __name__ == '__main__':
    main()
