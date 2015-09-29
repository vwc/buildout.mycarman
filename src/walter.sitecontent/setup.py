# -*- coding: utf-8 -*-
"""Installer for the walter.sitecontent package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = read('README.rst')

setup(
    name='walter.sitecontent',
    version='1.0.0',
    description="new sitecotent for mycarman",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='mycarman',
    author='John Doe',
    author_email='john@ade25.de',
    url='http://pypi.python.org/pypi/walter.sitecontent',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['walter'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.app.dexterity [grok, relations]',
        'plone.app.relationfield',
        'plone.namedfile [blobs]',
        'plone.formwidget.contenttree',
    ],
    extras_require={
        'test': [
            'mock',
            'plone.app.testing',
            'unittest2',
        ],
        'develop': [
            'coverage',
            'flake8',
            'jarn.mkrelease',
            'plone.app.debugtoolbar',
            'plone.reload',
            'Products.Clouseau',
            'Products.DocFinderTab',
            'Products.PDBDebugMode',
            'Products.PrintingMailHost',
            'Sphinx',
            'zest.releaser',
            'zptlint',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
