from zope.i18n import translate
from zope.component import getUtility
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage
from Products.Five import BrowserView

from plone.memoize.ram import cache
from ..interfaces import IDiagramProducer

def on_modification(func, view):
   "small caching helper utility"
   return view.context.modified()

#@cache(on_modification) # see above

class SVGDiagramView(BrowserView):
   ""

   def diagram(self):
      "return produced diagram"
      produce = getUtility(IDiagramProducer, name=self.context.producer)
      diagram = produce(self.context.source)
      return diagram[146:]
