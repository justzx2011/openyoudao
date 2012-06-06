#encoding=utf-8 
import webkit, gtk
import thread
import fusion
import webshot
import record_xclip
import random
import os
import time
from time import sleep
def lookup():
    sleep(5)
    global homedir
    homedir = os.getcwd()
    pre_text=""
    text=""
    global url
    url=""
    #监视history.txt变化
    cmd = "tail -f " + homedir + "/cache/history.cache"
    #print cmd
    #myfile=os.popen("tail -f \'" + homedir +"\' + \'"/cache/history.txt"\'")
    myfile=os.popen(cmd)
    while True:
        text=myfile.readline().strip('\r\n\x00')
        if (pre_text != text): 
            pre_text = text
            url="http://dict.youdao.com/search?q=" + text
            #tmp="curl -s -o " + homedir + "/cache/youdao.htm \'" + url+ "\'"
            #print tmp
            os.system("curl -s -o cache/youdao.html \'" + url+ "\'")
            fusion.reconstruct()
            homeurl="file://" + homedir + "/cache/result.html"
            window.load(homeurl)
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
    os.system("/bin/echo "" > cache/history.cache")
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
