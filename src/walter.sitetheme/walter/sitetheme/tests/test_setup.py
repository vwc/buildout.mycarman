# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from walter.buildout.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of walter.buildout into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if walter.buildout is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('walter.buildout'))

    def test_uninstall(self):
        """Test if walter.buildout is cleanly uninstalled."""
        self.installer.uninstallProducts(['walter.buildout'])
        self.assertFalse(self.installer.isProductInstalled('walter.buildout'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IWalterBuildoutLayer is registered."""
        from walter.buildout.interfaces import IWalterBuildoutLayer
        from plone.browserlayer import utils
        self.failUnless(IWalterBuildoutLayer in utils.registered_layers())
