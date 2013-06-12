#!/usr/bin/python

from gi.repository import Gtk
from main_window import MainWindow

win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
