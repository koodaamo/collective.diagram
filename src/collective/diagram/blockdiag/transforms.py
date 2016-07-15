import re
from blockdiag import parser, builder, drawer
from zope.interface import implementer
from plone.app.textfield.interfaces import ITransformer, TransformError
from Products.PortalTransforms.interfaces import ITransform


def create_diagram(diagram_txt):
   tree = parser.parse_string(diagram_txt)
   diagram = builder.ScreenNodeBuilder.build(tree)
   drawing = drawer.DiagramDraw('SVG', diagram) # DO NOT PASS FILENAME
   drawing.draw()
   return drawing.save()

"""
@implementer(ITransformer)
class DiagramToSVG(object):

   def __init__(self, context):
      self.context = context

   def __call__(self, value, mimeType):
      if not value.mimeType.startswith('text/'):
         raise TransformError("Can only work with text")
      if mimeType != 'text/x-blockdiag':
         raise TransformError("Mime type has to be text/x-blockdiag")
      return create_diagram(value)
"""


@implementer(ITransform)
class DiagramToSVGTransform(object):
   "Transform blockdiag to SVG"

   inputs = ("text/x-blockdiag",)
   output = "image/svg+xml"

   def name(self):
      "return the name of the transform instance"
      return "blockdiag_to_svg"

   def convert(self, data, idata, **kwargs):
      "convert the data, store the result in idata and return that"
      svg = create_diagram(data)
      idata.setData(svg[146:])
      return idata


def register():
    return DiagramToSVGTransform()
