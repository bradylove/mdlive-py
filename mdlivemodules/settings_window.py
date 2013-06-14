from gi.repository import Gtk

class SettingsWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,
                            type=Gtk.WindowType.TOPLEVEL,
                            title="MDLive Settings")
        self.set_border_width(5)

        self.set_default_size(600, 400)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,)
        self.add(self.box)

        self.notebook = Gtk.Notebook()
        self.notebook.set_tab_pos(Gtk.PositionType.TOP)

        self.markdown_extensions_page = Gtk.Grid()
        self.markdown_extensions_label = Gtk.Label("Markdown Extensions")

        self.render_flags_page = Gtk.Grid()
        self.render_flags_label = Gtk.Label("HTML Render Flags")

        self.notebook.append_page(self.markdown_extensions_page,
                                  self.markdown_extensions_label)
        self.notebook.append_page(self.render_flags_page,
                                  self.render_flags_label)

        self.close_button = Gtk.Button("_Close", use_underline=True)

        self.box.pack_start(self.notebook, True, True, 5)
        self.box.pack_start(self.close_button, False, True, 0)

        # Markdown Extentions
        no_intra_emph_check = Gtk.CheckButton("No Intra Emphasis")
        php_tables_check      = Gtk.CheckButton("Tables")
        fenced_code_check     = Gtk.CheckButton("Fenced Code Blocks")
        autolink_check        = Gtk.CheckButton("Autolinks")
        strikethrough_check   = Gtk.CheckButton("Strikethrough")
        lax_html_blocks_check = Gtk.CheckButton("Lax HTML Blocks")
        space_headers_check   = Gtk.CheckButton("Space Headers")
        super_script_check    = Gtk.CheckButton("Superscript")

        self.markdown_extensions_page.add(no_intra_emph_check)
        self.markdown_extensions_page.attach_next_to(php_tables_check,
                                                     no_intra_emph_check,
                                                     Gtk.PositionType.BOTTOM, 1, 2)
        self.markdown_extensions_page.attach_next_to(fenced_code_check,
                                                     php_tables_check,
                                                     Gtk.PositionType.BOTTOM, 1, 2)
        self.markdown_extensions_page.attach_next_to(autolink_check,
                                                     fenced_code_check,
                                                     Gtk.PositionType.BOTTOM, 1, 2)
        self.markdown_extensions_page.attach_next_to(strikethrough_check,
                                                     autolink_check,
                                                     Gtk.PositionType.BOTTOM, 1, 2)
        self.markdown_extensions_page.attach_next_to(lax_html_blocks_check,
                                                     strikethrough_check,
                                                     Gtk.PositionType.BOTTOM, 1, 2)
        self.markdown_extensions_page.attach_next_to(space_headers_check,
                                                     lax_html_blocks_check,
                                                     Gtk.PositionType.BOTTOM, 1, 2)
        self.markdown_extensions_page.attach_next_to(super_script_check,
                                                     space_headers_check,
                                                     Gtk.PositionType.BOTTOM, 1, 2)
        self.show_all()
