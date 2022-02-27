import re

import mistune
from mistune.util import escape_url


class UbbRenderer(mistune.HTMLRenderer):
    """UBB renderer for rendering Markdown.
    """

    def __init__(self, **kwargs):
        super(mistune.HTMLRenderer, self).__init__()
        self.options = kwargs

    def placeholder(self):
        return ''

    def paragraph(self, text):
        """Rendering paragraph tags. Like ``<p>``."""
        # return '<p>%s</p>\n' % text.strip(' ')
        return '%s\n' % text.strip(' ')

    def text(self, text):
        """Rendering unformatted text.

        :param text: text content.
        """
        if self.options.get('parse_block_html'):
            return text
        return text

    def double_emphasis(self, text):
        """Rendering **strong** text.

        :param text: text content for emphasis.
        """
        return '[b]%s[/b]' % text

    def heading(self, text, level, raw=None):
        """Rendering header/heading tags like ``<h1>`` ``<h2>``.

        :param text: rendered text content for the header.
        :param level: a number for the header level, for example: 1.
        :param raw: raw text content of the header.

        level1 to size7, level2 to size6 ...
        level6 to size2, size2 is the min value
        """
        if level <= 6:
            size = 8 - level
        else:
            size = level
        return '\n[b][size=%d]%s[/size][/b]\n\n' % (size, text)

    def strikethrough(self, text):
        """Rendering ~~strikethrough~~ text.

        :param text: text content for strikethrough.
        """
        return '[s]%s[/s]' % text

    def codespan(self, text):
        """Rendering inline `code` text.

        :param text: text content for inline code.
        """
        text = text.rstrip()
        return ' [b][color=#1E6BB8]%s[/color][/b] ' % text

    def thematic_break(self):
        return '\n[hr]\n'

    def link(self, link, title, text):
        """Rendering a given link with content and title.

        :param link: href link for ``<a>`` tag.
        :param title: title content for `title` attribute.
        :param text: text content for description.
        """
        link = escape_url(link)
        if not title:
            return '[url=%s]%s[/url]' % (link, text)

        return '[url=%s]%s[/url]' % (link, title)

    def linebreak(self):
        """Rendering line break like ``<br>``."""
        if self.options.get('use_xhtml'):
            return '\n'
        return '\n'

    def emphasis(self, text):
        """Rendering like _text_"""
        return '[i]' + text + '[/i]'

    def strong(self, text):
        return '[b]' + text + '[/b]'

    def block_code(self, code, lang=None):
        """Rendering block level code. ``pre > code``.

        :param code: text content of the code block.
        :param lang: language of the given code.
        """
        code = code.rstrip('\n')
        return '[code]%s\n[/code]\n' % code

    def block_quote(self, text):
        """Rendering <blockquote> with the given text.

        :param text: text content of the blockquote.
        """
        return '[quote]%s\n[/quote]\n' % text.rstrip('\n')

    def autolink(self, link, is_email=False):
        """Rendering a given link or email address.

        :param link: link content or email address.
        :param is_email: whether this is an email or not.
        """
        text = link
        return '[url=%s]%s[/url]' % (link, text)

    def list(self, body, ordered, level, start=None):
        """Rendering list tags like ``<ul>`` and ``<ol>``.

        :param body: body contents of the list.
        :param ordered: whether this list is ordered or not.
        """
        if ordered:
            tag = "[list=1]"
        else:
            tag = "[list]"
        return '%s\n%s[/list]\n' % (tag, body)

    def list_item(self, text, level):
        """Rendering list item snippet. Like ``<li>``."""
        return '[*]%s\n' % text

    def image(self, src, title, text):
        """Rendering a image with title and text.

        :param src: source link of the image.
        :param title: title text of the image.
        :param text: alt text of the image.
        """
        src = escape_url(src)
        html = '[img]%s[/img]' % src
        if self.options.get('use_xhtml'):
            return '%s' % html
        return '%s' % html

    def block_html(self, html):
        """Rendering block level pure html content.

        :param html: text content of the html snippet.
        """
        # print "block html: " + html
        if html.startswith("<!-- more -->"):
            return ''
        else:
            raise Exception("not support block_html like: " + html + " yet ..")

    def hrule(self):
        """Rendering method for ``<hr>`` tag."""
        return '[hr]\n'

    def inline_html(self, html):
        """Rendering span level pure html content.

        :param html: text content of the html snippet.
        """
        # print "inline html: " + html
        support_pattern = '<img src="(?P<img_src>.*)" .*>'
        m = re.search(support_pattern, html)
        if m:
            # print m.group("img_src")
            return '[img]%s[/img]' % m.group("img_src")
        else:
            raise Exception("not support inline_html like: " + html + " yet ..")

    def newline(self):
        """Rendering newline element."""
        return ''



