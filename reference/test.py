#!/usr/bin/env python

# Sam's Web Browser, a nice simple web browser that is most appropriately useless, like it's creator.

# Known bugs: Trying to open a new browser window is possible from the GUI, but does not work. You have to type "http://" before everything or it will not work. This is probably easy to fix but I am just lazy.

# Enjoy. Scores 100/100 on the Acid 3 test.

# Requires gtk and webkit.
import gtk
import webkit

# Create main window and it's properties.
window = gtk.Window()
window.set_title("USERNAME Browser")
window.resize(720, 480)
window.connect("delete-event", gtk.main_quit)

# Create the widgets.
address = gtk.Entry()

progress = gtk.ProgressBar()
progress.set_text("Page is loading, please wait..")

go = gtk.Button("Go")

about_button = gtk.Button("About")

search = gtk.Button("Search")

browser = webkit.WebView()

scroll = gtk.ScrolledWindow()
scroll.add(browser)

# About Dialog
about_dialog = gtk.AboutDialog()
about_dialog.set_comments("Simplicity and elegance.")
about_dialog.set_program_name("USERNAME Browser")
about_dialog.set_version("0.2")
about_dialog.set_license("GPL v2 or greater.")
about_dialog.set_website("http://www.debian.org/")
about_dialog.set_authors(["Samuel Orr"])
about_dialog.set_logo(None)

# Load a default page. This can be changed.
DEFAULT_URL = 'https://www.duckduckgo.com/'
url = DEFAULT_URL
browser.open(url)

# Define the horizontal widgets.
toolbar = gtk.HBox()
toolbar.pack_start(about_button, False)
toolbar.pack_start(address)
toolbar.pack_start(go, False)
toolbar.pack_start(search, False)

# Define the vertical widgets.
display = gtk.VBox()
display.pack_start(toolbar, False)
display.pack_start(scroll)
display.pack_start(progress, False)

# Function to define the load page button.
def goclicked(btn):
    browser.open(address.get_text())
    go.connect("clicked", goclicked)

# Function to load a page on key press.
def loadpagekey(key):
    browser.open(address.get_text())
    address.connect("activate", loadpagekey)

# Funtion to define the progress bar.
def load_progress_changed(webview, amount):
    progress.set_fraction(amount / 100.0)
    browser.connect("load-progress-changed", load_progress_changed)

# Function to show the progress bar during page load.
def load_started(webview, frame):
    progress.set_visible(True)
    browser.connect("load-started", load_started)

# Function to hide the progress bar when load is finished.
def load_finished(webview, frame):
    progress.set_visible(False)
    address.set_text(frame.get_uri())
    browser.connect("load_finished", load_finished)

# Function to define the about button.
def about_button_clicked(btn):
    about_dialog.run()
    about_dialog.hide()
    about_button.connect("clicked", about_button_clicked)

# Function to define the search button.
def search_button(btn):
    browser.open("https://www.duckduckgo.com/")
    search.connect("clicked", search_button)


# Show the widgets
window.add(display)
window.show_all()

# Start the program
gtk.main()
