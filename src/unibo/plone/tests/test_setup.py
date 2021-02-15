# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from unibo.plone.testing import UNIBO_PLONE_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that unibo.plone is properly installed."""

    layer = UNIBO_PLONE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if unibo.plone is installed."""
        self.assertTrue(self.installer.isProductInstalled("unibo.plone"))

    def test_browserlayer(self):
        """Test that IUniboPloneLayer is registered."""
        from plone.browserlayer import utils
        from unibo.plone.interfaces import IUniboPloneLayer

        self.assertIn(IUniboPloneLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = UNIBO_PLONE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstallProducts(["unibo.plone"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if unibo.plone is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled("unibo.plone"))

    def test_browserlayer_removed(self):
        """Test that IUniboPloneLayer is removed."""
        from plone.browserlayer import utils
        from unibo.plone.interfaces import IUniboPloneLayer

        self.assertNotIn(IUniboPloneLayer, utils.registered_layers())
