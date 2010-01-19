# -*- coding: utf-8 -*-
from trac.core import *

from trac.web.chrome import Chrome
from trac.wiki.api import parse_args
from trac.wiki.macros import WikiMacroBase
from trac.util.html import escape

class XspfSlimMacro(WikiMacroBase):
    def expand_macro(self, formatter, name, content):
        _, kw = parse_args(content)
        name = kw.get('name', 'Unknown')
        artist = kw.get('artist', 'Unknown')
        song_title = escape("%s - %s"%(name, artist))
        wiki = kw.get('wiki', formatter.resource.id)
        attachment = kw.get('attachment')
        song_url = "/raw-attachment/wiki/%s/%s"%(wiki, attachment)
        data = Chrome(self.env).populate_data(formatter.req, {
            'song_url': song_url,
            'song_title': song_title,
            'name': name,
            'artist': artist
        });
        return Chrome(self.env).load_template('xspf-slim.html').\
                generate(**data)

class XspfButtonMacro(WikiMacroBase):
    def expand_macro(self, formatter, name, content):
        _, kw = parse_args(content)
        name = kw.get('name', 'Unknown')
        wiki = kw.get('wiki', formatter.resource.id)
        artist = kw.get('artist', 'Unknown')
        attachment = kw.get('attachment')
        song_url = "/raw-attachment/wiki/%s/%s"%(wiki, attachment)
        data = Chrome(self.env).populate_data(formatter.req, {
            'song_url': song_url,
            'name': name,
            'artist': artist
        });
        return Chrome(self.env).load_template('xspf-button.html').\
                generate(**data)

