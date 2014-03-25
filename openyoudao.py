#!/usr/bin/python
#-*- coding: utf-8 -*-
# Simple demo for the RECORD extension
# Not very much unlike the xmacrorec2 program in the xmacro package.
import popen2
from time import sleep
import thread
import webshot
import sys
import fusionyoudao
import gl
import os
import webkit, gtk
import logging

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
            pipe = os.popen("xclip -o")
            text = pipe.readline()
            pipe.readlines()    #清空管道剩余部分
            pipe.close()
            text = text.strip('\r\n\x00').lower()
            if(gl.pre_text != text and text!=""):
			         gl.pre_text = text
				 if(False==os.path.exists(gl.cachedir)):
				     os.system("mkdir  \'" + gl.cachedir + "\'")
				     os.system("touch  \'" + gl.origindir + "\'")
				     os.system("touch  \'" + gl.resultdir + "\'")
			         url= "http://dict.youdao.com/search?q=" + text
                                 logging.debug(text)
			         os.system("curl -s -w %{http_code}:%{time_connect}:%{time_starttransfer}:%{time_total}:%{speed_download} -o \'" + gl.origindir +"\' \'" + url+ "\'")       #获得网页(非代理)
			         fusionyoudao.reconstruct()
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
  window.load(gl.indexurl)
  window.show()
  gtk.main()
  record_dpy.record_free_context(ctx)
  os.system("ps aux | grep openyoudao.py |awk '{print $2}' |xargs kill -9 >/dev/null")
  Alive=0

def gettext():
  record_dpy.record_enable_context(ctx,record_callback)
  record_dpy.record_free_context(ctx)
def lookup_keysym(keysym):
  for name in dir(XK):
    if name[:3] == "XK_" and getattr(XK, name) == keysym:
      return name[3:]
    return "[%d]" % keysym
def main():
  os.system("xclip -f /dev/null")           #清空剪切板
  logging.basicConfig(filename=gl.logname,
                     level=logging.DEBUG,
                     format="%(asctime)s - %(message)s")
  global Alive
  Alive=1
  thread.start_new_thread(webshow,())
  sleep(0.2)
  thread.start_new_thread(gettext,())
  while Alive:
	sleep(0.5)
        clip_id=os.popen("ps aux | grep xclip | grep -v grep |awk '{print $2}'| grep -v ^$ |wc -l")
        pid = clip_id.readline().strip('\r\n\x00')
        if int(pid)>=1:
            os.system("ps aux | grep xclip |awk '{print $2}' |xargs kill -9 >/dev/null")
if __name__ == '__main__':
	main()
