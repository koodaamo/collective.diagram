# -*- coding: utf-8 -*-

from zope.interface import implementer
from Products.CMFPlone.interfaces import INonInstallable
from Products.CMFCore.utils import getToolByName

from . import logger, MIME_TYPE, MIME_NAME, TRANSFORM_NAME


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        "Hide uninstall profile from site-creation and quickinstaller"
        return [
            'collective.diagram:uninstall',
        ]


#def isNotCurrentProfile(context):
#    return context.readDataFile("diagram_marker.txt") is None

def post_install(context):
    "Post install script"

    import pdb; pdb.set_trace()

    # Adding our mime type to MTR
    mtr = context.mimetypes_registry #getToolByName(site, 'mimetypes_registry')

    existing_mt = mtr.lookup(MIME_TYPE)
    if bool(existing_mt):
        # Already installed, delete what's there already in preparation for (re) install.
        logger.info("%s (%s) Mime type already installed, deleting", MIME_TYPE, MIME_NAME)
        mtr.manage_delObjects(existing_mt)

    mtr.manage_addMimeType(
        MIME_NAME,
        (MIME_TYPE,),
        ("diag",),
        "document_icon.png",
        binary=False,
        globs=("*.diag",))

    logger.info("%s (%s) Mime type installed", MIME_TYPE, MIME_NAME)

    # Registering our transform in PT
    ptt = context.portal_transforms
    if TRANSFORM_NAME not in ptt.objectIds():
        # Not already installed
        ptt.manage_addTransform(TRANSFORM_NAME, 'collective.diagram.transform')


def uninstall(context):
    "Uninstall script"

    import pdb; pdb.set_trace()
    # Removing our types from MTR
    try:
        context.mimetypes_registry.manage_delObjects((MIME_TYPE,))
    except:
       logger.warn("Could not remove '%s', already removed?" % MIME_TYPE)

    # Removing our transform from PT
    try:
       context.portal_transforms.unregisterTransform(TRANSFORM_NAME)
    except:
       logger.warn("Could not unregister '%s', already unregistered?" % TRANSFORM_NAME)

