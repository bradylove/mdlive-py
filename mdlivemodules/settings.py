import os
import configparser
import misaka

class Settings():
    def __init__(self):
        self.path   = self.settings_file_path()
        self.config = self.read_config()

    def read_config(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.path)

        return self.config

    def settings_file_path(self):
        home_dir = os.path.expanduser("~")
        path = os.path.join(home_dir, ".config", "mdlive", "settings")

        return path
    def save_setting(self, group, setting, value):
        self.config[group][setting] = str(value)
        with open(self.path, 'w') as configfile:
            self.config.write(configfile)

    def markdown_extensions(self):
        self.read_config()
        x = 0

        if self.get_extension_value("no_intra_emphasis"):
            x = x + misaka.EXT_NO_INTRA_EMPHASIS
        if self.get_extension_value("tables"):
            x = x + misaka.EXT_TABLES
        if self.get_extension_value("fenced_code_blocks"):
            x = x + misaka.EXT_FENCED_CODE
        if self.get_extension_value("autolink"):
            x = x + misaka.EXT_AUTOLINK
        if self.get_extension_value("strikethrough"):
            x = x + misaka.EXT_STRIKETHROUGH
        if self.get_extension_value("lax_html_blocks"):
            x = x + misaka.EXT_LAX_HTML_BLOCKS
        if self.get_extension_value("space_headers"):
            x = x + misaka.EXT_SPACE_HEADERS
        if self.get_extension_value("superscript"):
            x = x + misaka.EXT_SUPERSCRIPT

        return x

    def html_render_flags(self):
        self.read_config()
        x = 0

        if self.get_html_flag_value("skip_html"):
            x = x + misaka.HTML_SKIP_HTML
        if self.get_html_flag_value("skip_style"):
            x = x + misaka.HTML_SKIP_STYLE
        if self.get_html_flag_value("skip_images"):
            x = x + misaka.HTML_SKIP_IMAGES
        if self.get_html_flag_value("skip_links"):
            x = x + misaka.HTML_SKIP_LINKS
        if self.get_html_flag_value("safelink"):
            x = x + misaka.HTML_SKIP_LINKS
        if self.get_html_flag_value("toc"):
            x = x + misaka.HTML_TOC
        if self.get_html_flag_value("hardwrap"):
            x = x + misaka.HTML_HARD_WRAP
        if self.get_html_flag_value("use_xhtml"):
            x = x + misaka.HTML_USE_XHTML
        if self.get_html_flag_value("escape"):
            x = x + misaka.HTML_ESCAPE

    def get_bool(self, group, setting):
        return self.config.getboolean(group, setting)

    def get_html_flag_value(self, setting):
        return self.get_bool("HTML Render Flags", setting)

    def get_extension_value(self, setting):
        return self.get_bool("Markdown Extensions", setting)
