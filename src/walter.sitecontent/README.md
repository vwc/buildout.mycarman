# walter.sitecontent

## new sitecotent for mycarman

* `Source code @ GitHub <https://github.com/ade25/walter.sitecontent>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/walter.sitecontent>`_
* `Documentation @ ReadTheDocs <http://waltersitecontent.readthedocs.org>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/ade25/walter.sitecontent>`_

## How it works

This package provides a Plone addon as an installable Python egg package.

The generated Python package holds an example content type `ContentPage` which
provides a folderish version of the default **Page** document type.

The implementation is kept simple on purpose and asumes that the developer will
add further content manually.


## Installation

To install `walter.sitecontent` you simply add ``walter.sitecontent``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `walter.sitecontent` using the Add-ons control panel.
