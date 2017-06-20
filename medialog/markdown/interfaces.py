# -*- coding: utf-8 -*-
# Default ENCODING = 'UTF-8'

####################
from z3c.form import interfaces
from zope import schema
#from zope.interface import Interface
from zope.interface import alsoProvides
from plone.directives import form
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.markdown')

 