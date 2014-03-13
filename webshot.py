import sys
import gl
import os
import gtk
import time
import webkit
class OutputView(webkit.WebView):
    '''a class that represents the output widget of a conversation
    '''
    def __init__(self):
        webkit.WebView.__init__(self)
        self.load_finish_flag = False
        self.set_property('can-focus', True)
        self.set_property('can-default', True)
        self.set_full_content_zoom(1)
       # self.clipbord = gtk.Clipboard()
        #settings = self.get_settings()
        #try:
        #    settings.set_property('enable-universal-access-from-file-uris', True)
        #    settings.set_property('javascript-can-access-clipboard', False)
        #    settings.set_property('enable-default-context-menu', True)
        #    settings.set_property('enable-page-cache', True)
        #    settings.set_property('tab-key-cycles-through-elements', True)
        #    settings.set_property('enable-file-access-from-file-uris', True)
        #    settings.set_property('enable-spell-checking', False)
        #    settings.set_property('enable-caret-browsing', False)
        #    try:
        #         # Since 1.7.5
        #        settings.set_property('enable-accelerated-compositing', True)
        #    except TypeError:
        #         pass
        #except:
        #    print 'Error: settings property was not set.'


class Window(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.set_resizable(True)
        self.set_title("openyoudao")
        self.set_default_size(1024, 240)
        self.scroll = gtk.ScrolledWindow()
        self.scroll.props.hscrollbar_policy = gtk.POLICY_NEVER
        self.scroll.props.vscrollbar_policy = gtk.POLICY_NEVER
        self.output = OutputView()
        self.scroll.add(self.output)
        self.add(self.scroll)
        self.scroll.show_all()
        self.connect('delete-event', gtk.main_quit)
        #self.is_fullscreen = False
    def load(self, url):
        print url
        self.output.load_uri(url)
    def reload(self):
        self.output.reload()
        
#window = Window()
#window.load(sys.argv[1])
#window.load("http://dict.youdao.com/")
#window.show()
#gtk.main()
