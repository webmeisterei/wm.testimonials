.. contents::

Introduction
============

Creates a folder `testimonials` within your plone site.

If you're using `INavigationRoot` (eg for Microsites or mulitligual site) place
the `testimonials` folder directly into your navigation root folder.


Marker Interface: `ITestimonialFolder`


Testimonials are no extra content type - we use Images



Title
  Name and role of the person. eg: `Scott Tiger, CEO`

Description
  The statement text

Subject
  used to optionally categorize testimonials


Image
  Picture of the person

Related Content
  Can be used to link the statement with an other text


Managing Statements
-------------------

Categorize Statements by using Keywords



Portlet can display a single statement, a random statement out of all available
statements or a random statement with a certain subject


TODOS:
* support multiple views on the portlet as collectionmultiview portlet does.
* implement single testimonial and subject filtered testimonials

