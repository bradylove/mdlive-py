from gi.repository import Gtk
from gi.repository import WebKit
from mdlivemodules.menu_bar import MenuBar
from mdlivemodules.renderer import Renderer
from misaka import Markdown
from mdlivemodules.settings import Settings

import misaka
import houdini

import re, os

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,
                            type=Gtk.WindowType.TOPLEVEL,
                            title="MDLive Markdown Editor")
        self.version = "0.1.0"
        default_width  = 1280
        default_height = 720

        self.settings = Settings()

        self.set_default_size(default_width, default_height)
        self.set_position(Gtk.WindowPosition.MOUSE)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        self.menu_bar = MenuBar(self)

        self.split_box = Gtk.HPaned()
        self.split_box.set_position(default_width / 2)

        self.editor = Gtk.TextView()
        self.editor.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)

        self.editor_buffer = self.editor.get_buffer()
        self.editor_scroller = Gtk.ScrolledWindow()
        self.editor_scroller.add(self.editor)

        self.preview = WebKit.WebView()
        self.preview.open("file://" + self.installed_path() + "/assets/index.html")
        self.preview_scroller = Gtk.ScrolledWindow()
        self.preview_scroller.add(self.preview)

        self.split_box.add1(self.editor_scroller)
        self.split_box.add2(self.preview_scroller)

        self.box.pack_start(self.menu_bar, False, False, 0)
        self.box.pack_start(self.split_box, True, True, 0)

        self.renderer = Renderer()
        self.markdown = Markdown(self.renderer, extensions=self.settings.markdown_extensions())

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
        root = __file__
        if os.path.islink(root):
            root = os.path.realpath(root)
        return os.path.dirname(os.path.abspath(root))
        # return module_locator.module_path(self.installed_path)

    def get_setting_value(self, setting):
        config = Settings.read_settings_file()
        config.getboolean("Markdown Extensions", setting)

    def update_markdown(self):
        self.renderer = Renderer(flags=self.settings.html_render_flags())
        self.markdown = Markdown(self.renderer, extensions=self.settings.markdown_extensions())

        self.render_markdown()
