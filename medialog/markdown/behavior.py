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
    
    bodytext = schema.TextLine(
    	title=u"Body text",
    )
  
    form.widget(
          bodytext=MarkdownFieldWidget,
    )
          
alsoProvides(IMarkdownBehavior, IFormFieldProvider)


