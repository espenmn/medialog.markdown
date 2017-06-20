from zope import schema
from zope.interface import Interface
from zope.interface import implements
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory

from medialog.markdown.widgets.widget import MarkdownFieldWidget

_ = MessageFactory('medialog.markdown')

 
class IMarkdownBehavior(form.Schema):
    """ A markdown text field"""
    
    markdown = schema.TextLine(
        title = _("markdown", default=u"Markdown"),
        required = False,
        description = _("help_markdown",
                      default="Markdown text"),
    )

    form.widget(
        markdown=MarkdownFieldWidget,
    )

alsoProvides(IMarkdownBehavior, IFormFieldProvider)


