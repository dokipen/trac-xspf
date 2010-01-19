# -*- coding: utf-8 -*-
from trac.core import *

from trac.web.chrome import Chrome
from trac.wiki.api import parse_args
from trac.wiki.macros import WikiMacroBase
from trac.util.html import escape

class XspfButtonMacro(WikiMacroBase):
    def expand_macro(self, formatter, name, content):
        _, kw = parse_args(content)
        song_url = "/raw-attachment/wiki"\
                "/%s/%s"%(formatter.resource.id, kw.get('attachment'))
        name = kw.get('name', 'Unknown')
        artist = kw.get('artist', 'Unknown')
        song_title = escape("%s - %s"%(name, artist))
        data = Chrome(self.env).populate_data(formatter.req, {
            'song_url': song_url,
            'song_title': song_title,
            'name': name,
            'artist': artist
        });
        return Chrome(self.env).load_template('xspf.html').\
                generate(**data)

