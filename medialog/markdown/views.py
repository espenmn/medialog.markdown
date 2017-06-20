from Products.Five import BrowserView
from plone import api
#from medialog.markdown.interfaces import IIconPickerSettings

class RenderMarkdown(BrowserView):
    """ """
    
    def value(self):
    	return self.context
    	
    def xxxrender_html(self):
        """Return the preview as a stringified HTML document."""
        import pdb; pdb.set_trace()
        portal = plone.api.portal.get()
        convertTo = portal.portal_transforms.convertTo
        mimetype, data = self.request.form.items()[0]
        return convertTo("text/x-html-safe", data, mimetype=mimetype).getData()

    


   