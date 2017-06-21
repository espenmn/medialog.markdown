from zope import schema
from zope.interface import Interface
from plone.app.textfield import RichText
from zope.interface import implements
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory

from z3c.form.browser.textarea import TextAreaFieldWidget

#do I need this?
from plone.app.textfield.interfaces import IRichTextValue
from plone.app.textfield.interfaces import ITransformer


from medialog.markdown.widgets.widget import MarkdownFieldWidget

_ = MessageFactory('medialog.markdown')

 
class IMarkdownBehavior(form.Schema):
    """ A markdown text field"""
    
    markdown = schema.Text(
        title = _("markdown", default=u"Markdown"),
        required = False,
        description = _("help_markdown",
                      default="Markdown text"),
    )
  
    bodyText = RichText(
        title=u"Body text",
        default_mime_type='text/x-web-markdown',
        output_mime_type='text/html',
        allowed_mime_types=('text/x-web-markdown',),
        default=u"Default value"
    )
  
    form.widget(
          markdown=MarkdownFieldWidget,
          bodyText=MarkdownFieldWidget,
    )
          
alsoProvides(IMarkdownBehavior, IFormFieldProvider)


