#!/usr/bin/python
#-*- coding: utf-8 -*-
# RECORD extension
# Not very much unlike the xmacrorec2 program in the xmacro package.
import popen2
import  goslate
from time import sleep
import thread
import webshot
import sys
import fusionyoudao
import gl
import os
import webkit, gtk
# Change path so we find Xlib
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Xlib import X, XK, display
from Xlib.ext import record
from Xlib.protocol import rq
record_dpy = display.Display()

def record_callback(reply):
    if reply.category != record.FromServer:
        return
    if reply.client_swapped:
        print "* received swapped protocol data, cowardly ignored"
        return
    if not len(reply.data) or ord(reply.data[0]) < 2:
# not an event
        return
    data = reply.data
    while len(data):
        event, data = rq.EventField(None).parse_binary_value(data, record_dpy.display, None, None)

# deal with the event type
        if event.type == X.ButtonRelease:
            # get text
            global Alive
            pipe = os.popen("xclip -o")
            text = pipe.readline()
            pipe.readlines()    #清空管道剩余部分
            pipe.close()
            print "您选取的是: ", text
            text = text.strip('\r\n\x00').lower().strip()
            if(gl.pre_text != text and text!=""and gl.lock=="0" or text=="%lock%"):
                                 url = ""
			         gl.pre_text = text
				 if(False==os.path.exists(gl.cachedir)):
				     os.system("mkdir  \'" + gl.cachedir + "\'")
                                 for dir in (gl.origindir,gl.resultdir,gl.historydir,gl.keyworddir):
				     if(False==os.path.exists(dir)):
				         os.system("touch  \'" + dir + "\'")
                                 #youdao
                                 if "%zh2enlj%" in text:
                                     gl.homeurl="file:///usr/share/openyoudao/zh2enlj.html"
                                     gl.searchurl=gl.zh2enlj
                                     url = ""
                                     gl.func="lj"
                                     gl.Dict="youdao"
                                     gl.title="汉英例句"
                                 elif "%zh2japlj%" in text:
                                     gl.homeurl="file:///usr/share/openyoudao/zh2japlj.html"
                                     gl.searchurl=gl.zh2japlj
                                     url = ""
                                     gl.func="lj"
                                     gl.Dict="youdao"
                                     gl.title="汉日例句"
                                 elif "%zh2kolj%" in text:
                                     gl.homeurl="file:///usr/share/openyoudao/zh2kolj.html"
                                     gl.searchurl=gl.zh2kolj
                                     url = ""
                                     gl.func="lj"
                                     gl.Dict="youdao"
                                     gl.title="汉韩例句"
                                 elif "%zh2frlj%" in text:
                                     gl.homeurl="file:///usr/share/openyoudao/zh2frlj.html"
                                     gl.searchurl=gl.zh2frlj
                                     url = ""
                                     gl.func="lj"
                                     gl.Dict="youdao"
                                     gl.title="汉法例句"
                                 elif "%zh2en%" in text:
                                     gl.homeurl="file:///usr/share/openyoudao/zh2en.html"
                                     gl.searchurl=gl.zh2en
                                     url = ""
                                     gl.Dict="youdao"
                                     gl.title="汉英互译"
                                 elif "%zh2jap%" in text:
                                     gl.homeurl="file:///usr/share/openyoudao/zh2jap.html"
                                     gl.searchurl=gl.zh2jap
                                     url = ""
                                     gl.Dict="youdao"
                                     gl.title="汉日互译"
                                 elif "%zh2ko%" in text:
                                     gl.homeurl="file:///usr/share/openyoudao/zh2ko.html"
                                     gl.searchurl=gl.zh2ko
                                     url = ""
                                     gl.Dict="youdao"  
                                     gl.title="汉韩互译"
                                 elif "%zh2fr%" in text:
                                     gl.homeurl="file:///usr/share/openyoudao/zh2fr.html"
                                     gl.searchurl=gl.zh2fr
                                     url = ""
                                     gl.Dict="youdao"
                                     gl.title="汉法互译"

                                 #config
                                 elif "%index%" in text:
                                     gl.homeurl="file:///usr/share/openyoudao/config.html"
                                     url = ""
                                     gl.title="有道首页"
                                 elif "%helps%" in text:
                                     gl.homeurl="file:///usr/share/openyoudao/help.html"
                                     url = ""
                                     gl.title="使用说明"
                                 elif "%goslate%" in text:
                                     gl.homeurl="file:///usr/share/openyoudao/goslate.html"
                                     url = ""
                                     gl.Dict="google"
                                     gl.title="谷歌翻译"
                                 elif "%donate%" in text:
                                     gl.homeurl="file:///usr/share/openyoudao/donate.html"
                                     url = ""
                                     gl.title="捐赠页面"
                                 elif "%expand%" in text:
                                     gl.homeurl="file:///usr/share/openyoudao/expand.html"
                                     url = ""
                                     gl.title="展开选项"
                                 elif "%history%" in text:
                                     gl.homeurl= "file://" + gl.historydir
                                     if Alive==1:
                                         his_tar=open(gl.historydir,'w')
                                         print >> his_tar,"<!DOCTYPE html><html><head><meta charset=\"utf-8\"><title>History</title></head><body><p>%s&nbsp;&nbsp;&nbsp;&nbsp;%s</p>"%("%index%","%expand%") 
                                         keyword=open(gl.keyworddir,'r')
                                         print >> his_tar,keyword.read() 
                                         print >> his_tar,"</body></html>" 
                                         his_tar.close()
                                         keyword.close()
                                     url = ""
                                     gl.title="取词历史"
                                 elif "%lock%" in text:
                                     if gl.lock=="0":
                                         gl.lock="1"
                                         gl.homeurl="file:///usr/share/openyoudao/lock.html"
                                         gl.title="锁定取词"
                                     else:
                                         gl.lock="0"
                                         gl.homeurl="file:///usr/share/openyoudao/unlock.html"
                                         gl.title="取词解锁"
                                     url = ""
                                 elif "%exits%" in text:
                                     Alive=0
                                 else:
			             url= gl.searchurl + text
                                 if  url !="":
                                     if Alive==1:
                                         k_tar=open(gl.keyworddir,'a')
                                         print >> k_tar,"<p>%s</p>" % text
                                         k_tar.close()
                                         #fp = file(gl.keyworddir)
                                         #lines = []
                                         #for line in fp: # 内置的迭代器, 效率很高
                                         #    lines.append(line)
                                         #fp.close()
                                         #lines.insert(0, "<p>%s</p>" % text) # 在第二行插入
                                         #s = '\n'.join(lines)
                                         #fp = file(gl.keyworddir, 'w')
                                         #fp.write(s)
                                         #fp.close()
                                     #[google youdao]
                                     if gl.Dict=="google":
                                         gs = goslate.Goslate()
                                         gl.lang=gs.detect(text)
                                         g_tar=open(gl.googledir,'w+')
                                         if gl.lang=='zh-CN':
                                             basehtml="<!DOCTYPE html><html><head><meta charset=\"utf-8\"><title>Google Translate</title></head><body><p>Source Language：&nbsp;&nbsp;%s</p><p>Target Language :&nbsp;&nbsp;&nbsp;%s</p><p>Selected &nbsp;&nbsp;Text :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s</p><p>Target &nbsp;&nbsp;&nbsp;&nbsp;Text :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s</p><p>%s &nbsp;&nbsp;&nbsp;%s</p></body></html>"%(gl.lang,'en',text,gs.translate(text, 'en'),"%index%","%expand%")
                                         else:
                                             basehtml="<!DOCTYPE html><html><head><meta charset=\"utf-8\"><title>Google Translate</title></head><body><p>Source Language：&nbsp;&nbsp;%s</p><p>Target Language :&nbsp;&nbsp;&nbsp;%s</p><p>Selected &nbsp;&nbsp;Text :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s</p><p>Target &nbsp;&nbsp;&nbsp;&nbsp;Text :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s</p><p>%s &nbsp;&nbsp;&nbsp;%s</p></body></html>"%(gl.lang,'zh-CN',text,gs.translate(text, 'zh-CN'),"%index%","%expand%")
                                         print >> g_tar,basehtml
                                         g_tar.close()
                                         gl.homeurl= "file://" + gl.googledir
                                     if gl.Dict=="youdao":
			                 os.system("curl -s -w %{http_code}:%{time_connect}:%{time_starttransfer}:%{time_total}:%{speed_download} -o \'" + gl.origindir +"\' \'" + url+ "\'")       #获得网页(非代理)
			                 fusionyoudao.reconstruct(gl.func)
			                 gl.homeurl="file://" + gl.resultdir #合成最终缓冲访问地址
                                 if Alive==1:
			             window.settitle(gl.title)
			             window.load(gl.homeurl)
			             window.show()
if not record_dpy.has_extension("RECORD"):
  print "RECORD extension not found"
  sys.exit(1)
  r = record_dpy.record_get_version(0, 0)
  print "RECORD extension version %d.%d" % (r.major_version, r.minor_version)
# Create a recording context; we only want key and mouse events
ctx = record_dpy.record_create_context(
0,
[record.AllClients],
[{
'core_requests': (0, 0),
'core_replies': (0, 0),
'ext_requests': (0, 0, 0, 0),
'ext_replies': (0, 0, 0, 0),
'delivered_events': (0, 0),
'device_events': (X.KeyPress, X.MotionNotify),
'errors': (0, 0),
'client_started': False,
'client_died': False,
}])

def webshow():
  global window
  global Alive
  window = webshot.Window()
  window.load(gl.homeurl)
  window.show()
  gtk.main()
  record_dpy.record_free_context(ctx)
  os.system("ps aux | grep openyoudao.py |awk '{print $2}' |xargs kill -9 >/dev/null")
  Alive=0

def gettext():
  os.system("xclip -f /dev/null")           #清空剪切板
  record_dpy.record_enable_context(ctx,record_callback)
  record_dpy.record_free_context(ctx)
def main():
  global Alive
  Alive=1
  thread.start_new_thread(webshow,())
  sleep(0.5)
  thread.start_new_thread(gettext,())
  while Alive:
	sleep(0.2)
        clip_id=os.popen("ps aux | grep xclip | grep -v grep |awk '{print $2}'| grep -v ^$ |wc -l")
        pid = clip_id.readline().strip('\r\n\x00')
        if int(pid)>=1:
            os.system("ps aux | grep xclip |awk '{print $2}' |xargs kill -9 >/dev/null")
if __name__ == '__main__':
	main()
