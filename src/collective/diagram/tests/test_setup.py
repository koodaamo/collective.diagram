# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.diagram.testing import COLLECTIVE_DIAGRAM_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.diagram is properly installed."""

    layer = COLLECTIVE_DIAGRAM_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.diagram is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.diagram'))

    def test_browserlayer(self):
        """Test that IDiagramLayer is registered."""
        from collective.diagram.interfaces import (
            IDiagramLayer)
        from plone.browserlayer import utils
        self.assertIn(IDiagramLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_DIAGRAM_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.diagram'])

    def test_product_uninstalled(self):
        """Test if collective.diagram is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.diagram'))

    def test_browserlayer_removed(self):
        """Test that IDiagramLayer is removed."""
        from collective.diagram.interfaces import IDiagramLayer
        from plone.browserlayer import utils
        self.assertNotIn(IDiagramLayer, utils.registered_layers())
