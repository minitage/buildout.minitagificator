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








