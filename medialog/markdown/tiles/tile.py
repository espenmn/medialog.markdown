# -*- coding: utf-8 -*-

 
from plone.memoize.view import memoize
from plone.supermodel import model
from plone.tiles import PersistentTile
from plone.tiles.interfaces import ITileType
from zope import schema
from zope.component import getUtility
from zope.i18nmessageid import MessageFactory
from zope.interface import provider
from zope.schema import getFields

    
class IMarkdownTile(model.Schema):
    
    body = schema.Text(title=u"Rich text")
    
    
class MarkdownTile(PersistentTile):
    """A tile that displays image and richtext"""

