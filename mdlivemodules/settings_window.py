from gi.repository import Gtk
from mdlivemodules.settings import Settings

class SettingsWindow(Gtk.Window):
    def __init__(self, main_window):
        Gtk.Window.__init__(self,
                            type=Gtk.WindowType.TOPLEVEL,
                            title="MDLive Settings")

        self.main_window = main_window
        self.settings = Settings()

        self.connect("delete-event", self.hide_window)

        self.set_border_width(5)

        self.set_default_size(600, 400)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,)
        self.add(self.box)

        self.notebook = Gtk.Notebook()
        self.notebook.set_tab_pos(Gtk.PositionType.TOP)

        self.extensions_page = Gtk.Grid()
        self.extensions_label = Gtk.Label("Markdown Extensions")

        self.render_flags_page = Gtk.Grid()
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

        tables_check = Gtk.CheckButton("Tables", active=self.get_extension_value("tables"))
        tables_check.connect("toggled", self.setting_toggled, "tables")

        fenced_code_check = Gtk.CheckButton("Fenced Code Blocks", active=self.get_extension_value("fenced_code_blocks"))
        fenced_code_check.connect("toggled", self.setting_toggled, "fenced_code_blocks")

        autolink_check = Gtk.CheckButton("Autolinks", active=self.get_extension_value("autolink"))
        autolink_check.connect("toggled", self.setting_toggled, "autolink")

        strikethrough_check = Gtk.CheckButton("Strikethrough", active=self.get_extension_value("strikethrough"))
        strikethrough_check.connect("toggled", self.setting_toggled, "strikethrough")

        lax_html_blocks_check = Gtk.CheckButton("Lax HTML Blocks", active=self.get_extension_value("lax_html_blocks"))
        lax_html_blocks_check.connect("toggled", self.setting_toggled, "lax_html_blocks")

        space_headers_check = Gtk.CheckButton("Space Headers", active=self.get_extension_value("space_headers"))
        space_headers_check.connect("toggled", self.setting_toggled, "space_headers")

        superscript_check = Gtk.CheckButton("Superscript", active=self.get_extension_value("superscript"))
        superscript_check.connect("toggled", self.setting_toggled, "superscript")

        self.extensions_page.add(no_intra_emph_check)
        self.extensions_page.attach_next_to(tables_check,
                                            no_intra_emph_check,
                                            Gtk.PositionType.BOTTOM, 1, 2)
        self.extensions_page.attach_next_to(fenced_code_check,
                                            tables_check,
                                            Gtk.PositionType.BOTTOM, 1, 2)
        self.extensions_page.attach_next_to(autolink_check,
                                            fenced_code_check,
                                            Gtk.PositionType.BOTTOM, 1, 2)
        self.extensions_page.attach_next_to(strikethrough_check,
                                            autolink_check,
                                            Gtk.PositionType.BOTTOM, 1, 2)
        self.extensions_page.attach_next_to(lax_html_blocks_check,
                                            strikethrough_check,
                                            Gtk.PositionType.BOTTOM, 1, 2)
        self.extensions_page.attach_next_to(space_headers_check,
                                            lax_html_blocks_check,
                                            Gtk.PositionType.BOTTOM, 1, 2)
        self.extensions_page.attach_next_to(superscript_check,
                                            space_headers_check,
                                            Gtk.PositionType.BOTTOM, 1, 2)

    def setting_toggled(self, check_button, setting):
        value = check_button.get_active()
        self.settings.save_setting("Markdown Extensions", setting, value)
        self.main_window.update_markdown()

    def get_extension_value(self, setting):
        b = self.settings.get_extension_value(setting)
        return b

    def hide_window(self, caller, arg):
        self.hide_all()
