# -*- coding: utf-8 -*-

from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import alsoProvides
from zope.interface import implements
from zope.interface import Interface
#from collective import dexteritytextindexer
from plone.app.dexterity import textindexer
from plone.autoform.interfaces import IFormFieldProvider
#from plone.directives import form
from plone.supermodel import model
from plone.supermodel.model import Schema
from plone.autoform.directives import widget

from zope.i18nmessageid import MessageFactory

from medialog.markdown.widgets.widget import MarkdownFieldWidget

_ = MessageFactory('medialog.markdown')


class IMarkdownBehavior(Schema):
    """ A markdown text field"""

    textindexer.searchable('bodytext')

    bodytext = schema.Text(
    	title=u"Body text",
        description=u"Note: You can select text to preview, or preview all",
    )

    widget(
          bodytext=MarkdownFieldWidget,
    )


alsoProvides(IMarkdownBehavior, IFormFieldProvider)
