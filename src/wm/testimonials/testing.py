from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class WmtestimonialsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import wm.testimonials
        xmlconfig.file(
            'configure.zcml',
            wm.testimonials,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        
        # Installs all the Plone stuff. Workflows etc.
        self.applyProfile(portal, 'Products.CMFPlone:plone')
                
        applyProfile(portal, 'wm.testimonials:default')

WM_TESTIMONIALS_FIXTURE = WmtestimonialsLayer()
WM_TESTIMONIALS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(WM_TESTIMONIALS_FIXTURE,),
    name="WmtestimonialsLayer:Integration"
)
