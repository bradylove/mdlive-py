from gi.repository import Gtk
from mdlivemodules.settings import Settings

class SettingsWindow(Gtk.Window):
    def __init__(self, main_window):
        Gtk.Window.__init__(self,
                            type=Gtk.WindowType.TOPLEVEL,
                            title="MDLive Settings")

        self.main_window = main_window
        self.settings = Settings()
        self.set_modal(True)
        self.set_transient_for(self.main_window)

        self.set_border_width(5)

        self.set_default_size(600, 400)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,)
        self.add(self.box)

        self.notebook = Gtk.Notebook()
        self.notebook.set_tab_pos(Gtk.PositionType.TOP)

        self.extensions_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.extensions_label = Gtk.Label("Markdown Extensions")

        self.render_flags_page = Gtk.Box()
        self.render_flags_label = Gtk.Label("HTML Render Flags")

        self.notebook.append_page(self.extensions_page,
                                  self.extensions_label)
        self.notebook.append_page(self.render_flags_page,
                                  self.render_flags_label)

        self.close_button = Gtk.Button("_Close", use_underline=True)

        self.box.pack_start(self.notebook, True, True, 5)
        self.box.pack_start(self.close_button, False, True, 0)

        # Markdown Extentions
        no_intra_emph_check = Gtk.CheckButton("No Intra Emphasis", active=self.get_extension_value("no_intra_emphasis"))
        no_intra_emph_check.connect("toggled", self.setting_toggled, "no_intra_emphasis")
        self.extensions_page.pack_start(no_intra_emph_check, False, False, 0)

        tables_check = Gtk.CheckButton("Tables", active=self.get_extension_value("tables"))
        tables_check.connect("toggled", self.setting_toggled, "tables")
        self.extensions_page.pack_start(tables_check, False, False, 0)

        fenced_code_check = Gtk.CheckButton("Fenced Code Blocks", active=self.get_extension_value("fenced_code_blocks"))
        fenced_code_check.connect("toggled", self.setting_toggled, "fenced_code_blocks")
        self.extensions_page.pack_start(fenced_code_check, False, False, 0)

        autolink_check = Gtk.CheckButton("Autolinks", active=self.get_extension_value("autolink"))
        autolink_check.connect("toggled", self.setting_toggled, "autolink")
        self.extensions_page.pack_start(autolink_check, False, False, 0)

        strikethrough_check = Gtk.CheckButton("Strikethrough", active=self.get_extension_value("strikethrough"))
        strikethrough_check.connect("toggled", self.setting_toggled, "strikethrough")
        self.extensions_page.pack_start(strikethrough_check, False, False, 0)

        lax_html_blocks_check = Gtk.CheckButton("Lax HTML Blocks", active=self.get_extension_value("lax_html_blocks"))
        lax_html_blocks_check.connect("toggled", self.setting_toggled, "lax_html_blocks")
        self.extensions_page.pack_start(lax_html_blocks_check, False, False, 0)

        space_headers_check = Gtk.CheckButton("Space Headers", active=self.get_extension_value("space_headers"))
        space_headers_check.connect("toggled", self.setting_toggled, "space_headers")
        self.extensions_page.pack_start(space_headers_check, False, False, 0)

        superscript_check = Gtk.CheckButton("Superscript", active=self.get_extension_value("superscript"))
        superscript_check.connect("toggled", self.setting_toggled, "superscript")
        self.extensions_page.pack_start(superscript_check, False, False, 0)

        self.show_all()

    def setting_toggled(self, check_button, setting):
        value = check_button.get_active()
        self.settings.save_setting("Markdown Extensions", setting, value)
        self.main_window.update_markdown()

    def get_extension_value(self, setting):
        b = self.settings.get_extension_value(setting)
        return b
