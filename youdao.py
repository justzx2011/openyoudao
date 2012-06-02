#encoding=utf-8 
import webkit, gtk
import thread
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
    url=""
    #监视history.txt变化
    myfile=os.popen("tail -f history.txt")
    while True:
        text=myfile.readline()
        if (pre_text != text): 
            if (text != ""):
                pre_text = text
                url="http://dict.youdao.com/search?q=" + text
                browser.open(url) 
    
         
def webshow():
    global browser
    global Alive
    window = gtk.Window()
    browser = webkit.WebView()
    window.set_default_size(480,320)
    window.set_resizable(True)
    window.add(browser)
    window.show_all()
    browser.show()
    browser.load_uri("http://dict.youdao.com/search?q=")
    window.connect("delete-event", gtk.main_quit)
    window.set_title("有道字典")
    gtk.main()  
    Alive=0

def gettext():
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
