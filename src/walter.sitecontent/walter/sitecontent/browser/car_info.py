from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.ZCatalog.interfaces import ICatalogBrain

from plone.app.contentlisting.interfaces import IContentListingObject
from zope.component import getMultiAdapter

class CarInfo(BrowserView):
	""" show car info 
	"""
def __call__(self):
	return self.render()

def render(self):
	return self.index()

