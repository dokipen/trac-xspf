from trac.core import *
from trac.web.chrome import ITemplateProvider

class XspfView(Component):
    implements(ITemplateProvider)

    def get_templates_dirs(self):
        from pkg_resources import resource_filename
        return [resource_filename(__name__, 'templates')]

    def get_htdocs_dirs(self):
        from pkg_resources import resource_filename
        return [('tracxspf', resource_filename(__name__, 'htdocs'))]
