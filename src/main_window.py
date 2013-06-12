from gi.repository import Gtk
from gi.repository import WebKit
from menu_bar import MenuBar
from renderer import Renderer
from misaka import Markdown
import misaka
import houdini

import module_locator
import re

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,
                            type=Gtk.WindowType.TOPLEVEL,
                            title="MDLive Markdown Editor")
        self.version = "0.1.0"
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
        editor_scroller = Gtk.ScrolledWindow()
        editor_scroller.add(self.editor)

        self.preview = WebKit.WebView()
        self.preview.open("file://" + self.installed_path() + "/assets/index.html")
        preview_scroller = Gtk.ScrolledWindow()
        preview_scroller.add(self.preview)

        self.split_box.add1(editor_scroller)
        self.split_box.add2(preview_scroller)

        self.box.pack_start(self.menu_bar, False, False, 0)
        self.box.pack_start(self.split_box, True, True, 0)

        self.renderer = Renderer()
        self.markdown = Markdown(self.renderer, extensions=
                              misaka.EXT_FENCED_CODE |
                              misaka.EXT_AUTOLINK |
                              misaka.EXT_SPACE_HEADERS)

        self.editor_buffer.connect("end-user-action", self.on_buffer_end_user_action)

    def on_buffer_end_user_action(self, buffer):
        self.render_markdown()

    def render_markdown(self):
        start, end = self.editor_buffer.get_bounds()

        text    = self.editor_buffer.get_text(start, end, True)
        results = self.markdown.render(text)
        escaped = houdini.escape_js(results)

        if escaped == None:
            escaped = houdini.escape_js("\n")

        self.preview.execute_script("window.App.setHtml('" + escaped + "')")

    def installed_path(self):
        return module_locator.module_path(self.installed_path)
