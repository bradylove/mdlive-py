from gi.repository import Gtk

class FileSaver():
    def __init__(self, parent):
        self.parent = parent

        dialog = Gtk.FileChooserDialog("Please choose a file", self.parent,
                                       Gtk.FileChooserAction.SAVE,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_SAVE, Gtk.ResponseType.OK))

        dialog.set_do_overwrite_confirmation(True)

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            self.save_file(dialog.get_filename())

        dialog.destroy()

    def save_file(self, file_path):
        file = open(file_path, "w+")

        buffer = self.parent.editor_buffer
        start, end = buffer.get_bounds()
        text = buffer.get_text(start, end, False)

        file.write(text)
        file.close()
