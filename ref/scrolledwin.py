#!/usr/bin/env python

# example scrolledwin.py

import pygtk
pygtk.require('2.0')
import gtk

class ScrolledWindowExample:
    def destroy(self, widget):
        gtk.main_quit()

    def __init__(self):
        # Create a new dialog window for the scrolled window to be
        # packed into. 
        window = gtk.Dialog()
        window.connect("destroy", self.destroy)
        window.set_title("ScrolledWindow example")
        window.set_border_width(0)
        window.set_size_request(300, 300)

        # create a new scrolled window.
        scrolled_window = gtk.ScrolledWindow()
        scrolled_window.set_border_width(10)

        # the policy is one of POLICY AUTOMATIC, or POLICY_ALWAYS.
        # POLICY_AUTOMATIC will automatically decide whether you need
        # scrollbars, whereas POLICY_ALWAYS will always leave the scrollbars
        # there. The first one is the horizontal scrollbar, the second, the
        # vertical.
        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)

        # The dialog window is created with a vbox packed into it.
        window.vbox.pack_start(scrolled_window, True, True, 0)
        scrolled_window.show()
    
        # create a table of 10 by 10 squares.
        table = gtk.Table(10, 10, False)

        # set the spacing to 10 on x and 10 on y
        table.set_row_spacings(10)
        table.set_col_spacings(10)

        # pack the table into the scrolled window
        scrolled_window.add_with_viewport(table)
        table.show()

        # this simply creates a grid of toggle buttons on the table
        # to demonstrate the scrolled window.
        for i in range(10):
            for j in range(10):
                buffer = "button (%d,%d)" % (i, j)
                button = gtk.ToggleButton(buffer)
                table.attach(button, i, i+1, j, j+1)
                button.show()

        # Add a "close" button to the bottom of the dialog
        button = gtk.Button("close")
        button.connect_object("clicked", self.destroy, window)

        # this makes it so the button is the default.
        button.set_flags(gtk.CAN_DEFAULT)
        window.action_area.pack_start( button, True, True, 0)

        # This grabs this button to be the default button. Simply hitting
        # the "Enter" key will cause this button to activate.
        button.grab_default()
        button.show()
        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ScrolledWindowExample()
    main()
