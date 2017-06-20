import zope.component
import zope.interface
import zope.schema.interfaces

from z3c.form import interfaces
from z3c.form import widget
from z3c.form.browser import text

from plone import api
#from medialog.markdown.interfaces import IMarkdownSettings


class IMarkdownWidget(interfaces.IWidget):
    """Markdown widget."""
 

class MarkdownWidget(text.TextWidget):
    """Markdown Widget"""
    
    def render_html(self):
        """Return the preview as a stringified HTML document."""
        portal_transforms = api.portal.get_tool(name='portal_transforms')
        value = self.value
        data = portal_transforms.convertTo('text/html', value, mimetype='text/x-web-markdown')
        html = data.getData()
        return html

    zope.interface.implementsOnly(IMarkdownWidget)
    
        
def MarkdownFieldWidget(field, request):
    """IFieldWidget factory for MarkdownWidget."""
    return widget.FieldWidget(field, MarkdownWidget(request))
    
    
    
