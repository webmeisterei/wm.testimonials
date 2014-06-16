from zope.interface import Interface
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

from zope import schema
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFPlone import PloneMessageFactory as __

from urlparse import urlsplit, urlunsplit
from random import getrandbits
from Products.CMFPlone.utils import safe_hasattr
from plone.memoize.instance import memoize
from wm.testimonials.util import getTestimonialFolder



class ITestimonialPortlet(IPortletDataProvider):
    """
    """

    #category - show all of a category

    #testimonial - show single testimonial



class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(ITestimonialPortlet)

    def __init__(self, category=None, testimonial=None):
        self.category = category
        self.testimonial = testimonial



    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        if self.category:
            return u"Testimonials for %s" % self.category
        if self.testimonial:
            return u"Testimonial %s" % self.testimonial.UID()
        return u"Random testimonial"



class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('testimonial.pt')


    @property
    def testimonialFolder(self):
        return getTestimonialFolder(context)



    def getTestimonials(self):

        if self.data.testimonial:
            return [self.data.testimonial]

        #TODO: use @@testimonials.testimonials here

        query = {}

        if self.data.category:
            query['Subject'] = self.data.category

        if self.testimonialFolder is None:
            return []

        result = []



        for item in self.testimonialFolder.listFolderContents(query):
            if '|' in item.Title():
                name, role = item.Title().split('|')
            else:
                name = item.Title()
                role = u''

            link = None
            if item.getRelatedItems():
                link = item.getRelatedItems()[0].absolute_url()

            result.append(dict(name=name.strip(),
                               role=role.strip(),
                               text = item.Description().replace('\n', '<br/>'),
                               link = link,
                               img = item,
                               ))
        return result


# NOTE: If this portlet does not have any configurable parameters, you can
# inherit from NullAddForm and remove the form_fields variable.

class AddForm(base.NullAddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """

    def create(self):
        return Assignment()



class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(ITestimonialPortlet)
