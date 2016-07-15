# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.diagram


class CollectiveDiagramLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.diagram)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.diagram:default')


COLLECTIVE_DIAGRAM_FIXTURE = CollectiveDiagramLayer()


COLLECTIVE_DIAGRAM_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_DIAGRAM_FIXTURE,),
    name='CollectiveDiagramLayer:IntegrationTesting'
)


COLLECTIVE_DIAGRAM_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_DIAGRAM_FIXTURE,),
    name='CollectiveDiagramLayer:FunctionalTesting'
)


COLLECTIVE_DIAGRAM_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_DIAGRAM_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveDiagramLayer:AcceptanceTesting'
)
