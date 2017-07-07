# -*- coding: utf-8 -*-

#from plone import api

from plone.memoize.view import memoize
from plone.supermodel import model
#from plone.tiles import Tile
from zope import schema
from plone.directives import form
from zope.i18nmessageid import MessageFactory
from plone.tiles import Tile
from zope.interface import provider
#from collective import dexteritytextindexer
from zope.schema import getFields


from medialog.markdown.interfaces import IMarkdownSettings
from medialog.markdown.widgets.widget import MarkdownFieldWidget
_ = MessageFactory('medialog.markdownn')


#ITile.implementedBy(MarkdownTile)

class IMarkdownTile(model.Schema):

    #dexteritytextindexer.searchable('bodytext')

    bodytext = schema.Text(
    	title=u"Body text",
    )

    form.widget(
          bodytext=MarkdownFieldWidget,
    )


class MarkdownTile(Tile):
    """A tile that displays markdown text"""

    def __init__(self, context, request):
        super(MarkdownTile, self).__init__(context, request)
