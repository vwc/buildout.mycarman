# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from walter.walter.buildout.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of walter.walter.buildout into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if walter.walter.buildout is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('walter.walter.buildout'))

    def test_uninstall(self):
        """Test if walter.walter.buildout is cleanly uninstalled."""
        self.installer.uninstallProducts(['walter.walter.buildout'])
        self.assertFalse(self.installer.isProductInstalled('walter.walter.buildout'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IWalterWalter.buildoutLayer is registered."""
        from walter.walter.buildout.interfaces import IWalterWalter.buildoutLayer
        from plone.browserlayer import utils
        self.failUnless(IWalterWalter.buildoutLayer in utils.registered_layers())
