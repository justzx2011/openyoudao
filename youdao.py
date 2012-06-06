#encoding=utf-8 
import webkit, gtk
import thread
import webshot
import record_xclip
import random
import os
import time
from time import sleep
from Queue import Queue
def lookup():
    sleep(5)
    pre_text=""
    text=""
    global url
    url=""
    #监视history.txt变化
    myfile=os.popen("tail -f history.txt")
    while True:
        text=myfile.readline().strip('\r\n\x00')
        if (pre_text != text): 
            pre_text = text
            url="http://dict.youdao.com/search?q=" + text
            window.reconstruction(url)
            #sleep(1)
            window.load('file:///home/zbn/workplace/openyoudao/history.html')
            window.show() 

def webshow():
    global window
    global Alive
    window = webshot.Window()
    window.load("http://dict.youdao.com/")
    window.show() 
    gtk.main() 
    Alive=0

def gettext():
    os.system("/bin/echo "" > history.txt")
    record_xclip.record_dpy.record_enable_context(record_xclip.ctx, record_xclip.record_callback)            
    record_xclip.record_dpy.record_free_context(record_xclip.ctx)
# Main thread
def main():

    thread.start_new_thread(gettext,())
    thread.start_new_thread(lookup,())
    thread.start_new_thread(webshow,())
    	
    #运行标志结束 
    global Alive
    Alive=1
    while Alive:
        sleep(1)

    print 'All threads have terminated.'
if __name__ == '__main__':
    main()
