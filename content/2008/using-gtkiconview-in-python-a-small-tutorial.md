Title: Using GtkIconView in Python: a small tutorial
Date: 2008-04-15 15:24
Author: admin
Category: Linux, Programmazione, Python
Tags: gtk, gtkiconview, gtkliststore, HowTo, programming, Python, tutorial
Slug: using-gtkiconview-in-python-a-small-tutorial
Status: published

In these days I was looking for a simple tutorial to understand how to
use **GtkIconView**, but the only thing I was able to find was an
example in PHP-Gtk. So I decided to translate it in **Python** language,
thinking it would be useful for other people trying to use that Gtk
control. You can find the code here:

\[sourcecode language='python'\]  
import gtk  
import gobject

DEFAULT\_IMAGE\_WIDTH = 100

\# Main Window setup  
window = gtk.Window(gtk.WINDOW\_TOPLEVEL)  
window.set\_size\_request(400, 240)  
window.connect("destroy", gtk.main\_quit)  
window.set\_title("Python GtkIconView Test")

\# Add a VBox  
vbox = gtk.VBox()  
window.add(vbox)

\# Setup Scrolled Window  
scrolled\_win = gtk.ScrolledWindow()  
scrolled\_win.set\_policy(gtk.POLICY\_AUTOMATIC, gtk.POLICY\_AUTOMATIC)

\# Setup ListStore to contain images and description  
model = gtk.ListStore(gtk.gdk.Pixbuf, gobject.TYPE\_STRING)

\# Create a tuple with image files  
immagini = ("BD786-TFR.jpg", "guido\_sottozero.jpg", "IMG\_0056.JPG",
"movies\_card.jpg")

for im in immagini:  
try:  
pixbuf = gtk.gdk.pixbuf\_new\_from\_file(im)  
pix\_w = pixbuf.get\_width()  
pix\_h = pixbuf.get\_height()  
new\_h = (pix\_h \* DEFAULT\_IMAGE\_WIDTH) / pix\_w \# Calculate the
scaled height before resizing image  
scaled\_pix = pixbuf.scale\_simple(DEFAULT\_IMAGE\_WIDTH, new\_h,
gtk.gdk.INTERP\_TILES)  
model.append((scaled\_pix, im))  
except:  
pass

\# Setup GtkIconView  
view = gtk.IconView(model) \# Pass the model stored in a ListStore to
the GtkIconView  
view.set\_pixbuf\_column(0)  
view.set\_text\_column(1)  
view.set\_selection\_mode(gtk.SELECTION\_MULTIPLE)  
view.set\_columns(0)  
view.set\_item\_width(150)

\# Pack objects and show them all  
scrolled\_win.add(view)  
vbox.pack\_start(scrolled\_win)  
window.show\_all()

gtk.main()  
\[/sourcecode\]

The important thing to notice is that you have to store all the images
in a **GtkListStore** and pass it to the **GtkIconView** as *"model"*
parameter. I hope this example is clear. If you have any question,
please comment this post and I'll try to answer.

This is a screenshot of this example:

![gtkiconview](http://www.andreagrandi.it/wp-content/uploads/2008/04/gtkiconview_sample.png)
