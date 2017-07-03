# -*- coding: utf-8 -*-

from plone import api

from plone.memoize.view import memoize
from plone.supermodel import model
from plone.tiles import PersistentTile
from zope import schema
from zope.i18nmessageid import MessageFactory

#from plone.registry.interfaces import IRegistry
3from zope.interface import provider

from zope.schema import getFields

from plone.tiles.interfaces import ITileType
from medialog.markdown.interfaces import IMarkdownSettings
from medialog.markdown.widgets.widget import MarkdownFieldWidget

_ = MessageFactory('medialog.markdownn')


class IMultiTile(model.Schema):
    
    dexteritytextindexer.searchable('bodytext')
    
    bodytext = schema.Text(
    	title=u"Body text",
    )
  
    form.widget(
          bodytext=MarkdownFieldWidget,
    )

    def make_button(self, name, icon, buttontext):
        group = 'group' + name
        name = 'cmd' + name
        title = name
        icon = icon
        buttontext = buttontext
        lenght = len(buttontext)
        return  """{
          name: '%(group)s',
          data: [{
            name: '%(name)s',
            toggle: true, // this param only take effect if you load bootstrap.js
            title: '%(title)s',
            icon: '%(icon)s',
            buttontext: '%(buttontext)s',
            callback: function(e) {
            // Append/remove admonion before the selection
                var chunk, cursor, selected = e.getSelection(),
                  content = e.getContent(),
                  pointer, prevChar;

                if (selected.length === 0) {
                  // Give extra word
                  chunk = e.__localize('tekst');
                } else {
                  chunk = selected.text;
                }
                e.replaceSelection('%(buttontext)s' + chunk);
                cursor = selected.start + %(lenght)i - 1;
                

                // Set the cursor
                e.setSelection(cursor, cursor + chunk.length);
                }
              }]
            },
            """ % {   'group' : group,
              'name'   : name,
              'title'  : title,
              'icon'   : icon,
              'buttontext' : buttontext,
              'lenght' : lenght,
            }
              
    def make_buttons(self):
        buttons = ""
        btns = api.portal.get_registry_record(name="button_pairs", interface=IMarkdownSettings)
        for btn in btns:
            buttons += self.make_button(btn['name'], btn['icon'], btn['buttontext'])
        return """<script>
          require([
          'jquery',
          '++resource++medialog.markdown/markdown.min',
          '++resource++medialog.markdown/bootstrap-markdown.min',
          ], function($) {
              $(".markdown-textarea").markdown({
              fullscreen:false,
              resize: 'vertical',
              language: 'nb',
              hiddenButtons: 'cmdPreview', 
              disabledButtons: 'cmdPreview', 
              additionalButtons: [
            [%(buttons)s]
          ]
        })
          });
        </script>""" % { 'buttons': buttons }
        
    def render_markdown(self):
        """Return the preview as a stringified HTML document."""
        portal_transforms = api.portal.get_tool(name='portal_transforms')
        value = self.value.encode('utf-8')
        data = portal_transforms.convertTo('text/html', value, mimetype='text/x-web-markdown')
        html = data.getData()
        return html
    
    
    def live_preview(self):
        return api.portal.get_registry_record(name="live_preview", interface=IMarkdownSettings)



    

    
    