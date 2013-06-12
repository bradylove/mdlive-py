from gi.repository import Gtk
from file_opener import FileOpener
from file_saver import FileSaver
from about_dialog import AboutDialog

class MenuBar(Gtk.MenuBar):
    def __init__(self, parent):
        Gtk.MenuBar.__init__(self)

        self.parent = parent

        # Build top level menu items
        file_menu_item = Gtk.MenuItem(label="File")
        edit_menu_item = Gtk.MenuItem(label="Edit")
        view_menu_item = Gtk.MenuItem(label="View")
        help_menu_item = Gtk.MenuItem(label="Help")

        # Add top level menu items to the menu bar
        self.add(file_menu_item)
        self.add(edit_menu_item)
        self.add(view_menu_item)
        self.add(help_menu_item)

        # Assign the submenus to the menu items
        file_menu_item.set_submenu(self.file_submenu())
        edit_menu_item.set_submenu(self.edit_submenu())
        view_menu_item.set_submenu(self.view_submenu())
        help_menu_item.set_submenu(self.help_submenu())

    def file_submenu(self):
        file_menu = Gtk.Menu()

        open_menu_item = Gtk.MenuItem(label="Open")
        save_menu_item = Gtk.MenuItem(label="Save")
        quit_menu_item = Gtk.MenuItem(label="Quit")

        file_menu.add(open_menu_item)
        file_menu.add(save_menu_item)
        file_menu.add(Gtk.SeparatorMenuItem())
        file_menu.add(quit_menu_item)

        open_menu_item.connect("activate", self.on_open_menu_activate)
        save_menu_item.connect("activate", self.on_save_menu_activate)
        quit_menu_item.connect("activate", Gtk.main_quit)

        return file_menu

    def edit_submenu(self):
        edit_menu = Gtk.Menu()

        return edit_menu

    def view_submenu(self):
        view_menu = Gtk.Menu()

        toggle_preview_menu_item = Gtk.MenuItem(label="Hide Preview")
        toggle_editor_menu_item  = Gtk.MenuItem(label="Hide Editor")

        view_menu.add(toggle_preview_menu_item)
        view_menu.add(toggle_editor_menu_item)

        toggle_preview_menu_item.connect("activate", self.on_toggle_preview_activate)
        toggle_editor_menu_item.connect("activate", self.on_toggle_editor_activate)

        return view_menu

    def help_submenu(self):
        help_menu = Gtk.Menu()

        about_menu_item = Gtk.MenuItem(label="About")

        help_menu.add(about_menu_item)

        about_menu_item.connect("activate", self.on_about_menu_activate)

        return help_menu

    def on_open_menu_activate(self, menu_item):
        FileOpener(self.parent)

    def on_save_menu_activate(self, menu_item):
        FileSaver(self.parent)

    def on_toggle_preview_activate(self, menu_item):
        text = menu_item.get_label()

        if text == "Hide Preview":
            self.parent.preview_scroller.hide()
            menu_item.set_label("Show Preview")
        elif text == "Show Preview":
            self.parent.preview_scroller.show()
            menu_item.set_label("Hide Preview")

    def on_toggle_editor_activate(self, menu_item):
        text = menu_item.get_label()

        if text == "Hide Editor":
            self.parent.editor_scroller.hide()
            menu_item.set_label("Show Editor")
        elif text == "Show Editor":
            self.parent.editor_scroller.show()
            menu_item.set_label("Hide Editor")

    def on_about_menu_activate(self, menu_item):
        AboutDialog(self.parent)
