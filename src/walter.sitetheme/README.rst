====================
walter.sitetheme
====================

Site theme package for the walter project based on Diazo and
plone.app.theming

* `Source code @ GitHub <https://github.com/ade25/walter.sitetheme>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/walter.sitetheme>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/ade25/walter.sitetheme>`_

How it works
============

This package provides the scaffolding for a full featured Plone theme. It does
setup a resource directory but does not provide the actual theme. The generation
of the actual theme compontents is left to the more appropriate toolchain
provided by state of the art frontend development.

At the time of writing this does require the user to generate a theme
infrastructure by running the `generator-diazotheme` via `yeoman` provided by
git@github.com:ade25/generator-diazotheme.git


Installation
============

To install `walter.sitetheme` you simply add ``walter.sitetheme``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `walter.sitetheme` using the Add-ons control panel.
