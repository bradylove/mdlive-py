import os
import configparser
import misaka

class Settings():
    def read_settings_file():
        path = Settings.settings_file_path()
        config = configparser.ConfigParser()
        config.read(path)

        return config

    def settings_file_path():
        home_dir = os.path.expanduser("~")
        path = os.path.join(home_dir, ".config", "mdlive", "settings")

        return path

    def save_setting(group, setting, value):
        path = Settings.settings_file_path()
        config = Settings.read_settings_file()
        config[group][setting] = value
        with open(path, 'w') as configfile:
          config.write(configfile)



    def get_extension_value(setting):
        config = Settings.read_settings_file()
        return config.getboolean("Markdown Extensions", setting)

    def get_extensions_total():
        x = 0

        if Settings.get_extension_value("no_intra_emphasis"):
            x = x + misaka.EXT_NO_INTRA_EMPHASIS
        if Settings.get_extension_value("tables"):
            x = x + misaka.EXT_TABLES
        if Settings.get_extension_value("fenced_code_blocks"):
            x = x + misaka.EXT_FENCED_CODE
        if Settings.get_extension_value("autolink"):
            x = x + misaka.EXT_AUTOLINK
        if Settings.get_extension_value("strikethrough"):
            x = x + misaka.EXT_STRIKETHROUGH
        if Settings.get_extension_value("lax_html_blocks"):
            x = x + misaka.EXT_LAX_HTML_BLOCKS
        if Settings.get_extension_value("space_headers"):
            x = x + misaka.EXT_SPACE_HEADERS
        if Settings.get_extension_value("superscript"):
            x = x + misaka.EXT_SUPERSCRIPT

        return x
