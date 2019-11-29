.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

===========
unibo.plone
===========

Tell me what your product does

Features
--------

- Monkey patch to `Catalog.safe_callable` avoid indexing object with the same name as index or metadata fields.
  (refs. https://community.plone.org/t/wrong-indexing-content/6025).
- Requires `experimental.noacquisition` and set `DRY_RUN` to `False`.
- Requires `collective.purgebyid`.

Examples
--------

This add-on can be seen in action at the following sites:
- Is there a page on the internet where everybody can see the features?


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Installation
------------

Install unibo.plone by adding it to your buildout::

    [buildout]

    ...

    eggs =
        unibo.plone


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/unibo.plone/issues
- Source Code: https://github.com/collective/unibo.plone
- Documentation: https://docs.plone.org/foo/bar


License
-------

The project is licensed under the GPLv2.
