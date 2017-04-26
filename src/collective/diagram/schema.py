from z3c.relationfield.schema import RelationChoice
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.formwidget.contenttree import PathSourceBinder
from plone.formwidget.contenttree import UUIDSourceBinder

from plone.supermodel import model
from zope.schema import Text, Choice
#from Products.CMFCore.interfaces import IFolderish
from Products.CMFCore.interfaces._content import IFolderish

from . import _


class IDiagramSchema(model.Schema):
    "schema for diagram content type"

    directives.widget('source', rows=10)
    source = Text(
        title=_(u'Diagram source'),
        description=_(u'Diagram markup source'),
        required=True
    )

    producer = Choice(
        title=_(u'Producer'),
        description=_(u'The method to use for producing the diagram from the source markup'),
        vocabulary="collective.diagram.producers",
        required=True
    )

    iconfolder = RelationChoice(
        title=_(u'Icon folder'),
        description=_(u'The folder in which diagram icons are stored'),
        source=ObjPathSourceBinder(navigation_tree_query=dict(portal_type=["Folder"]))
    )

    preceding_content = RichText(
        title=_(u'Preceding content'),
        description=_(u'Optional content shown above diagram on the page.'),
        required=False
    )

    following_content = RichText(
        title=_(u'Following content'),
        description=_(u'Optional content shown below diagram on the page.'),
        required=False
    )

