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

        self.render_flags_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.render_flags_label = Gtk.Label("HTML Render Flags")

        self.notebook.append_page(self.extensions_page,
                                  self.extensions_label)
        self.notebook.append_page(self.render_flags_page,
                                  self.render_flags_label)

        self.close_button = Gtk.Button("_Close", use_underline=True)

        self.box.pack_start(self.notebook, True, True, 5)
        self.box.pack_start(self.close_button, False, True, 0)

        # Markdown Extentions
        self.ext_check_button_for("no_intra_emphasis", "No Intra Emphasis")
        self.ext_check_button_for("tables", "Tables")
        self.ext_check_button_for("fenced_code_blocks", "Fenced Code Blocks")
        self.ext_check_button_for("autolink", "Autolink")
        self.ext_check_button_for("strikethrough", "Strikethrough")
        self.ext_check_button_for("lax_html_blocks", "Lax HTML Blocks")
        self.ext_check_button_for("space_headers", "Space Headers")
        self.ext_check_button_for("superscript", "Superscript")

        # HTML Render Flags
        self.flag_check_button_for("skip_html", "Skip HTML")
        self.flag_check_button_for("skip_style", "Skip Style")
        self.flag_check_button_for("skip_images", "Skip Images")
        self.flag_check_button_for("skip_links", "Skip Links")
        self.flag_check_button_for("safelink", "Safelink")
        self.flag_check_button_for("toc", "TOC")
        self.flag_check_button_for("hardwrap", "Hard wrap")
        self.flag_check_button_for("use_xhtml", "Use XHTML")
        self.flag_check_button_for("escape", "Escape")


        self.show_all()

    def flag_check_button_for(self, setting, label):
        self.check_button_for(setting, label, self.render_flags_page, "HTML Render Flags")

    def ext_check_button_for(self, setting, label):
        self.check_button_for(setting, label, self.extensions_page, "Markdown Extensions")

    def check_button_for(self, setting, label, page, group):
        btn = Gtk.CheckButton(label, active=self.get_value(group, setting))
        btn.connect("toggled", self.setting_toggled, group, setting)
        page.pack_start(btn, False, False, 0)

    def setting_toggled(self, check_button, group, setting):
        value = check_button.get_active()
        self.settings.save_setting(group, setting, value)
        self.main_window.update_markdown()

    def get_value(self, group, setting):
        b = self.settings.get_bool(group, setting)
        return b
