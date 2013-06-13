from gi.repository import Gtk

class AboutDialog(Gtk.AboutDialog):
    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self)
        self.set_program_name("MDLive")
        self.set_authors(['Brady Love'])
        self.set_version(parent.version)
        self.set_copyright("(c) Brady Love")
        self.set_comments("Live markdown editor using Misaka (Sundown) renderer \nand Pygments for syntax highlighting.")
        self.set_website("https://github.com/bradylove/mdlive")

        self.run()
        self.destroy()
