.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.diagram
==============================================================================

Provides support for generating diagrams from source markup.

Features
--------

- custom "diagram" content type with a diagram SVG view
- _blockdiag diagram support

Installation
------------

Install collective.diagram by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.diagram


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.diagram/issues
- Source Code: https://github.com/collective/collective.diagram

License
-------

The project is licensed under the GPLv2.


.. _blockdiag: http://www.blockdiag.com
