from Products.CMFCore.utils import getToolByName
from zope.component._api import getMultiAdapter

def testimonial2Dict(item):
    """returns a dictionary representation of a
    testimonial item (object - not brain)
    """

    if '|' in item.Title():
        name, role = item.Title().split('|')
    else:
        name = item.Title()
        role = u''

    link = None
    if item.getRelatedItems():
        link = item.getRelatedItems()[0].absolute_url()

    return dict(name=name.strip(),
                role=role.strip(),
                text=item.Description().replace('\n', '<br/>'),
                link=link,
                img=item,
                )

def getTestimonialFolder(context, request=None):
    """Returns the testimonials folder located in the "nearest"
    INavigationRoot. If there is none, return the one located in
    the plonesite.
    returns None if no testimonals folder could be found.
    """

    cat = getToolByName(context, 'portal_catalog')
    if request is None:
        request = context.REQUEST
    portal_state = getMultiAdapter((context, request),
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
