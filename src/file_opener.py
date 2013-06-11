from gi.repository import Gtk

class FileOpener():
    def __init__(self, parent):
        self.parent = parent

        dialog = Gtk.FileChooserDialog("Please choose a file", self.parent,
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        self.add_filters(dialog)

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("File selected: " + dialog.get_filename())
            self.open_file(dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Markdown files")
        filter_text.add_mime_type("text/x-markdown")
        dialog.add_filter(filter_text)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_mime_type("*")
        dialog.add_filter(filter_any)

    def open_file(self, file_path):
        file = open(file_path, "r")
        text = file.read()

        buffer = self.parent.editor_buffer

        start, end = buffer.get_bounds()

        buffer.delete(start, end)
        buffer.set_text(text, len(text))
