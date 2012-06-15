#encoding=utf-8 
import sqlite3
import gl
import sys
import webkit, gtk
import thread
import fusion
import webshot
import record_xclip
import random
import os
import StringIO
import time
from time import sleep
#global keywordtext
#global baseurl
#global prebaseurl
#global homedir
#global url
#keywordtext = ""
#baseurl=""
#prebaseurl=""
#url=""
#homedir = os.getcwd()
def inputconfig():
    gl.prebaseurl = gl.baseurl
    conn = sqlite3.connect('/home/justzx/.local/share/webkit/databases/file__0.localstorage')
    c = conn.cursor()
    c1 = conn.cursor()
    c.execute("select value from ItemTable where key = 'dict' ")
    c1.execute("select value from ItemTable where key = 'keyword' ")
    r= c.fetchone()
    r1= c1.fetchone()
    output=StringIO.StringIO() 
    output1=StringIO.StringIO() 
    print >>output,r[0]
    print >>output1,r1[0]
    #print gl.baseurl,output.getvalue()
    #print gl.keywordtext,output1.getvalue()
    gl.baseurl=str(output.getvalue())
    if(gl.prebaseurl != gl.baseurl):
        gl.keywordtext=str(output1.getvalue())
        oldStdout = sys.stdout
        sys.stdout= open("cache/history.cache", "w+")
        print >> sys.stdout,gl.keywordtext.strip()
    output.close()
    output1.close()
def lookup():
    sleep(5)
    pre_text=""
    text=""
    #监视history.txt变化
    cmd = "tail -f " + homedir + "/cache/history.cache"
    inputconfig()
    print gl.baseurl
    #myfile=os.popen("tail -f \'" + homedir +"\' + \'"/cache/history.txt"\'")
    myfile=os.popen(cmd)
    while True:
        text=myfile.readline().strip('\r\n\x00')
        if (pre_text != text): 
            pre_text = text
            url= gl.baseurl + text
            #tmp="curl -s -o " + homedir + "/cache/youdao.htm \'" + url+ "\'"
            #print tmp
            os.system("curl -s -o cache/youdao.html \'" + url+ "\'")
            os.system("echo "" > cache/result.html")
            fusion.reconstruct()
            homeurl="file://" + homedir + "/cache/result.html"
            window.load(homeurl)
            window.show() 

def webshow():
    global window
    global Alive
    global homedir
    homedir = os.getcwd()
    window = webshot.Window()
    #window.load("http://dict.youdao.com/")
    window.load("file://" + homedir + "/cache/config.html")
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
