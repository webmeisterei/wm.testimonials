import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from wm.testimonials.testing import \
    WM_TESTIMONIALS_INTEGRATION_TESTING
from wm.testimonials import FOLDER_ID


class TestExample(unittest.TestCase):

    layer = WM_TESTIMONIALS_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')



    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product
            installed
        """
        pid = 'wm.testimonials'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')


        self.assertTrue(FOLDER_ID in self.portal.objectIds(), 'Testimonials folder has not been created')
