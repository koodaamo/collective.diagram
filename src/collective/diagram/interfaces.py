# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.interface import Interface, Attribute
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IDiagramLayer(IDefaultBrowserLayer):
   "Marker interface that defines a browser layer."


class IDiagramProducer(Interface):
   ""

   name = Attribute("producer name")
   description = Attribute("producer description")

   def __call__():
      "produce a diagram from source definition"
