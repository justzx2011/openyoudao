#encoding=utf-8 
import sqlite3
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
def inputconfig():
    global keywordtext
    keywordtext = ""
    global baseurl
    baseurl=""
    global prebaseurl
    prebaseurl=""
    prebaseurl = baseurl
    conn = sqlite3.connect('/home/justzx/.local/share/webkit/databases/file__0.localstorage')
    homedir = os.getcwd()
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
    print baseurl,output.getvalue()
    print keywordtext,output1.getvalue()
    baseurl=str(output.getvalue())
    keywordtext=str(output1.getvalue())
    if(prebaseurl != baseurl):
        text=str(output1.getvalue())
        #print keywordtext
        #os.system("/bin/echo -e  \'"+ keywordtext + "\' >> cache/history.cache")
        oldStdout = sys.stdout
        sys.stdout= open("cache/history.cache", "w+")
        print >> sys.stdout,url.strip()
    prebaseurl=baseurl
    output.close()
    output1.close()
def lookup():
    sleep(5)
    global homedir
    homedir = os.getcwd()
    pre_text=""
    text=""
    global url
    url=""
    global baseurl
    #监视history.txt变化
    cmd = "tail -f " + homedir + "/cache/history.cache"
    inputconfig()
    print baseurl
    #myfile=os.popen("tail -f \'" + homedir +"\' + \'"/cache/history.txt"\'")
    myfile=os.popen(cmd)
    while True:
        text=myfile.readline().strip('\r\n\x00')
        if (pre_text != text): 
            pre_text = text
            url= baseurl + text
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
