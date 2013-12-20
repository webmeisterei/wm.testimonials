from Products.CMFCore.utils import getToolByName
from zope.component._api import getMultiAdapter


def getTestimonialFolder(self):
    """Returns the testimonials folder located in the "nearest"
    INavigationRoot. If there is none, return the one located in
    the plonesite.
    returns None if no testimonals folder could be found.
    """
    
    cat = getToolByName(self.context, 'portal_catalog')
    portal_state = getMultiAdapter((self.context, self.request),
                                   name=u'plone_portal_state')
    navigation_root_path = portal_state.navigation_root_path()
    folders = cat(path=navigation_root_path,
                  object_provides='wm.testimonials.interfaces.ITestimonialFolder')
    
    # if no testimonial folder has been found we search within the plonesite
    # note that this implementation does not support multiple navigationroots within the acquisition chain
    if len(folders)==0:
        folders = cat(object_provides='wm.testimonials.interfaces.ITestimonialFolder')            
    
    if len(folders)==0:
        return None
    
    return folders[0].getObject()