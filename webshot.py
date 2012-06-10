import sys
import os
import gtk
import time
import webkit
class OutputView(webkit.WebView):
    '''a class that represents the output widget of a conversation
    '''
    def __init__(self):
        webkit.WebView.__init__(self)
class Window(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.set_resizable(True)
        self.set_title("openyoudao")
        self.set_default_size(480, 320)
        self.output = OutputView()
        self.add(self.output)
        self.show_all()
        self.connect('delete-event', gtk.main_quit)
        self.is_fullscreen = False
    def load(self, url):
        self.output.load_uri(url)
        
#window = Window()
#window.load(sys.argv[1])
#window.load("http://dict.youdao.com/")
#window.show()
#gtk.main()
