#!/usr/bin/python
#-*- coding: utf-8 -*-
# Simple demo for the RECORD extension
# Not very much unlike the xmacrorec2 program in the xmacro package.

import sys
import os

# Change path so we find Xlib
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Xlib import X, XK, display
from Xlib.ext import record
from Xlib.protocol import rq

local_dpy = display.Display()
record_dpy = display.Display()
global pre_text
pre_text=""
def lookup_keysym(keysym):
    for name in dir(XK):
        if name[:3] == "XK_" and getattr(XK, name) == keysym:
            return name[3:]
            return "[%d]" % keysym

def record_callback(reply):
    if reply.category != record.FromServer:
        return
    if reply.client_swapped:
        print "* received swapped protocol data, cowardly ignored"
        return
    if not len(reply.data) or ord(reply.data[0]) < 2:
        return

    data = reply.data
    while len(data):
        event, data = rq.EventField(None).parse_binary_value(data, record_dpy.display, None, None)
    
    # deal with the event type
    if event.type == X.ButtonRelease:
        print "ButtonRelease", event.detail
        #print "\033[31mI'll emit a signal using dbus.\033[00m"
        print "\n",

        # get text
        pipe = os.popen("xclip -o")
        text = pipe.read()
        print "您抹黑的是: ", text
        pipe.close()
        
        global pre_text
        if(pre_text != text):
            pre_text = text
            # get result
            #buffer = "./google_translate.py en zh-CN \"" + text + "\""
            #pipe = os.popen(buffer)
            #result = pipe.read()
            #pipe.close()
            print text
        
        else:
            print "我不翻译"


# Check if the extension is present
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

# Enable the context; this only returns after a call to record_disable_context,
# while calling the callback function in the meantime
record_dpy.record_enable_context(ctx, record_callback)

# Finally free the context
record_dpy.record_free_context(ctx)
