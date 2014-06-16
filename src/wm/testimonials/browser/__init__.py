from Products.Five.browser import BrowserView
from wm.testimonials.util import getTestimonialFolder
from wm.testimonials.util import testimonial2Dict

class TestimonialsView(BrowserView):

    def testimonials(self, category=None, query_params={}):
        """returns all testimonials for the given category
        additional catalog query parameters can be given via

        query_params = {'sort_on': 'effective'}
        """

        testimonialFolder = getTestimonialFolder(self.context, self.request)
        query = {}
        if category is not None:
            query['Subject'] = category
        if testimonialFolder is None:
            return []

        query.update(query_params)

        result = []
        for item in testimonialFolder.listFolderContents(query):
            result.append(testimonial2Dict(item))

        return result
