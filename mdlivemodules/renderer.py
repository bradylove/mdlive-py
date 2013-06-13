from misaka import HtmlRenderer
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

class Renderer(HtmlRenderer):
    def block_code(self, text, lang):
        if lang == None:
            lang = "bash"
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(text, lexer, formatter)
