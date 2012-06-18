#encoding=utf-8 
import sqlite3
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
def inputconfig():
    gl.prebaseurl = gl.baseurl
    conn = sqlite3.connect('/home/justzx/.local/share/webkit/databases/file__0.localstorage')
    c = conn.cursor()
    c1 = conn.cursor()
    c.execute("select value from ItemTable where key = 'dict' ")
    c1.execute("select value from ItemTable where key = 'keyword' ")
    r= c.fetchone()
    r1= c1.fetchone()
    gl.baseurl= "".join(str(r[0]).split('\x00')) #str to string
    #gl.keywordtext= "".join(str(r1[0]).split('\x00'))
    if(gl.prebaseurl != gl.baseurl) and (gl.prebaseurl != ""):   #switch to the selected dict and transfer the keyword
        os.system("/bin/echo -e  \'"+ "".join(str(r1[0]).split('\x00')) + "\' >> cache/history.cache")
    c.close()
    c1.close()
    conn.close
def lookup():
    sleep(5)
    pre_text=""
    text=""
    #监视history.txt变化
    cmd = "tail -f " + homedir + "/cache/history.cache"
    if(gl.baseurl==""):
        gl.baseurl="http://dict.youdao.com/search?q="
    #myfile=os.popen("tail -f \'" + homedir +"\' + \'"/cache/history.txt"\'")
    myfile=os.popen(cmd)
    #print gl.baseurl
    #print gl.prebaseurl
    while True:
        text=myfile.readline().strip('\r\n\x00')
        if (pre_text != text):
            pre_text = text
            url= gl.baseurl + text
            #tmp="curl -s -o " + homedir + "/cache/youdao.htm \'" + url+ "\'"
            print url + "kkkkkkkkkkkk"
            if(gl.baseurl==gl.baseurlyoudao):
                os.system("curl -s -o cache/youdao.html \'" + url+ "\'")
                os.system("echo "" > cache/result.html")
                fusionyoudao.reconstruct()
            elif(gl.baseurl==gl.baseurlicb):
                os.system("curl -s -o cache/icb.html \'" + url+ "\'") 
                os.system("echo "" > cache/result.html")
                fusionicb.reconstruct()
            homeurl="file://" + homedir + "/cache/result.html"
            window.load(homeurl)
            window.show()
        elif(gl.baseurl != gl.prebaseurl):
            url= gl.baseurl + text
            #tmp="curl -s -o " + homedir + "/cache/youdao.htm \'" + url+ "\'"
            #print url + "kkkkkkkkkkkk"
            if(gl.baseurl==gl.baseurlyoudao):
                os.system("curl -s -o cache/youdao.html \'" + url+ "\'")
                os.system("echo "" > cache/result.html")
                fusionyoudao.reconstruct()
            elif(gl.baseurl==gl.baseurlicb):
                os.system("curl -s -o cache/icb.html \'" + url+ "\'") 
                os.system("echo "" > cache/result.html")
                fusionicb.reconstruct()
            homeurl="file://" + homedir + "/cache/result.html"
            window.load(homeurl)
            window.show()
 

def webshow():
    global window
    global Alive
    global homedir
    homedir = os.getcwd()
    window = webshot.Window()
    window.load("file://" + homedir + "/cache/config.html")
    window.show() 
    gtk.main() 
    Alive=0

def gettext():
    os.system("/bin/echo "" > cache/history.cache")
    record_xclip.record_dpy.record_enable_context(record_xclip.ctx, record_xclip.record_callback)            
    record_xclip.record_dpy.record_free_context(record_xclip.ctx)
def loadconfig():
    while Alive :
        os.system("inotifywait -e modify /home/justzx/.local/share/webkit/databases/file__0.localstorage")
        inputconfig()
        #modify= "inotifywait -m -e modify /home/justzx/.local/share/webkit/databases/file__0.localstorage"
        #myfile=os.popen(modify)
        #if myfile.readline().find("MODIFY")==0:
        #    inputconfig() 
# Main thread
def main():

    thread.start_new_thread(gettext,())
    thread.start_new_thread(lookup,())
    thread.start_new_thread(webshow,())
    thread.start_new_thread(loadconfig,())
    	
    #运行标志结束 
    global Alive
    Alive=1
    while Alive:
        sleep(1)
        

    print 'All threads have terminated.'
if __name__ == '__main__':
    main()
