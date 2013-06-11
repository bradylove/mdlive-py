from gi.repository import Gtk
from gi.repository import WebKit
from menu_bar import MenuBar


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,
                            type=Gtk.WindowType.TOPLEVEL,
                            title="MDLive Markdown Editor")

        default_width  = 1280
        default_height = 720

        self.set_default_size(default_width, default_height)
        self.set_position(Gtk.WindowPosition.MOUSE)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        self.menu_bar = MenuBar(self)

        self.split_box = Gtk.HPaned()
        self.split_box.set_position(default_width / 2)


        self.editor = Gtk.TextView()
        self.editor_buffer = self.editor.get_buffer()

        self.preview = WebKit.WebView()
        self.preview.open("http://google.com")

        self.split_box.add1(self.editor)
        self.split_box.add2(self.preview)

        self.box.pack_start(self.menu_bar, False, False, 0)
        self.box.pack_start(self.split_box, True, True, 0)
