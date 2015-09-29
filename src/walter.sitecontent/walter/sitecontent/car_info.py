
# -*- coding: utf-8 -*-
"""Module providing project reference content type"""

from plone.dexterity.content import Container
from plone.directives import form
from plone.namedfile.interfaces import IImageScaleTraversable
from zope.interface import implementer
from zope import schema

from walter.sitecontent import _


class ICarInfo(form.Schema, IImageScaleTraversable):
    """ A folderish project reference
        This package has a soft dependency on ade25.assetmanager which
        is used as data provider and content source
    """
    form.order_after(reference='*')
    reference = schema.List(
        title=_(u"Car References"),
        required=False,
        value_type=schema.TextLine(
            title=_(u"Reference")
        )
    )


@implementer(ICarInfo)
class CarInfo(Container):
    pass