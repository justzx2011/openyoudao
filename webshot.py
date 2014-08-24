#!/usr/bin/python 
#-*- coding: utf-8 -*-
import sys
import gl
import os
#import gtk
import time
from gi.repository import Gdk,Gtk,GLib,WebKit

#import webkit

#class OutputView(WebKit.WebView):
    #'''a class that represents the output widget of a conversation
    #'''
    #def __init__(self):
        #WebKit.WebView.__init__(self)
        #self.load_finish_flag = False
        #self.set_property('can-focus', True)
        #self.set_property('can-default', True)
        #self.set_full_content_zoom(1)
       ## self.clipbord = gtk.Clipboard()
        #settings = self.get_settings()
        ##try:
        ##    settings.set_property('enable-universal-access-from-file-uris', True)
        ##    settings.set_property('javascript-can-access-clipboard', False)
        #settings.set_property('enable-default-context-menu', False)
        ##    settings.set_property('enable-page-cache', True)
        ##    settings.set_property('tab-key-cycles-through-elements', True)
        ##    settings.set_property('enable-file-access-from-file-uris', True)
        ##    settings.set_property('enable-spell-checking', False)
        ##    settings.set_property('enable-caret-browsing', False)
        ##    try:
        ##         # Since 1.7.5
        ##        settings.set_property('enable-accelerated-compositing', True)
        ##    except TypeError:
        ##         pass
        ##except:
        ##    print 'Error: settings property was not set.'


class Window(Gtk.Window):
    def __init__(self):
        print "lcq"
        Gtk.Window.__init__(self)
        #self.set_resizable(True)
        self.set_title("有道首页")
        self.set_default_size(800, 280)
        #self.set_icon_from_file("/usr/share/openyoudao/images/icon/icon.jpg")
        #self.scroll.props.hscrollbar_policy = Gtk.POLICY_NEVER
        #self.scroll.props.vscrollbar_policy = Gtk.POLICY_NEVER
        self.output = WebKit.WebView.new()
        self.scroll = Gtk.ScrolledWindow()

        self.scroll.add(self.output)
        self.add(self.scroll)
        #self.scroll.show_all()
        self.connect('delete-event', Gtk.main_quit)
        #self.is_fullscreen = False
    def load(self, url):
        print url
        self.output.load_uri(url)
    def reload(self):
        self.output.reload()
    def settitle(self,title):
        self.set_title(title)
        
#window = Window()
#window.load(sys.argv[1])
#window.load("http://dict.youdao.com/")
#window.show()
#gtk.main()
