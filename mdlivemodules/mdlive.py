#!/usr/bin/python

from gi.repository import Gtk
from mdlivemodules.main_window import MainWindow

def start():
    win = MainWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
