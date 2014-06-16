from Products.CMFCore.utils import getToolByName
from wm.testimonials import FOLDER_ID
from wm.testimonials.interfaces import ITestimonialFolder
from zope.interface.declarations import alsoProvides
from Products.CMFPlone.utils import _createObjectByType

def importVarious(context):
    """Miscellaneous steps import handle
    """

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    if context.readDataFile('wm.testimonials_various.txt') is None:
        return

    portal = context.getSite()

    customSetupRoutine(portal)


def customSetupRoutine(portal):
    """to be able to call the method w/o creating a fake context in
    the unittest, we added this method.
    """

    if FOLDER_ID in portal.objectIds():
        return

    portal.invokeFactory('Folder', id=FOLDER_ID, title=u"Testimonials")
    folder = portal.unrestrictedTraverse(FOLDER_ID)
    folder._md['excludeFromNav'] = True
    alsoProvides(folder, ITestimonialFolder)

    folder.setConstrainTypesMode(1)
    folder.setLocallyAllowedTypes(['Image'])

    wft = getToolByName(portal, 'portal_workflow')
    wft.doActionFor(folder, 'publish')

    folder.reindexObject()
