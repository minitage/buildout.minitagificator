
.. contents::

Introduction
============


    - This packages aims to replace some buildout parts by minitage's ones.
    - It replaces:

        - All zc.recipe.egg recipes but zc.recipe.custom:develop
        - zc.buildout.easy_install.install.Installer
        - zc.recipe.cmmi


Installation
=============

    - just add *buildout.minitagificator* to your buildout 's extension variable like ::

        [buildout]
        extensions = buildout.minitagificator

Makina Corpus sponsored software
======================================
|makinacom|_

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact us <mailto:python@makina-corpus.org>`_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com





TIPS
========

    -   set ``minitage-globalenv`` in buildout for the extension to set cflags
        and other things borrowed from the project minibuild if any.




