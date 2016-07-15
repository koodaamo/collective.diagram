from zope.interface import implementer
from ..interfaces import IDiagramProducer

from blockdiag import parser, builder, drawer


@implementer(IDiagramProducer)
class BlockdiagProducer(object):
   "utility (factory) that returns a callable (component)"

   name = u"blockdiag producer"
   description = u"produces diagram from blockdiag markup source"

   def __call__(self, source):
      tree = parser.parse_string(source)
      diagram = builder.ScreenNodeBuilder.build(tree)
      drawing = drawer.DiagramDraw('SVG', diagram) # DO NOT PASS FILENAME
      drawing.draw()
      return drawing.save()
