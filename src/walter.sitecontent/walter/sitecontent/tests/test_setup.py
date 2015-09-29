# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from walter.sitecontent.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of walter.sitecontent into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if walter.sitecontent is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('walter.sitecontent'))

    def test_uninstall(self):
        """Test if walter.sitecontent is cleanly uninstalled."""
        self.installer.uninstallProducts(['walter.sitecontent'])
        self.assertFalse(self.installer.isProductInstalled('walter.sitecontent'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IWalterSitecontentLayer is registered."""
        from walter.sitecontent.interfaces import IWalterSitecontentLayer
        from plone.browserlayer import utils
        self.failUnless(IWalterSitecontentLayer in utils.registered_layers())
