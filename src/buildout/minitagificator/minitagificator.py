

#!/usr/bin/env python


# Copyright (C) 2009, Mathieu PASQUET <mpa@makina-corpus.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

__docformat__ = 'restructuredtext en'

from minitage.recipe.egg import Recipe as Egg
from minitage.recipe.scripts import Recipe as Script
from copy import copy
import sys
import zc.buildout.easy_install

def install(buildout=None):

    recipe = Egg(buildout, 'foo', buildout['buildout'])

    def install(specs, dest,
                links=(), index=None,
                executable=recipe.executable, always_unzip=None,
                path=None, working_set=None, newest=True, versions=None,
                use_dependency_links=None, allow_hosts=('*',)):
        r = copy(recipe)
        r.eggs = specs
        r._dest = dest
        if links:
            r.find_links = links
        if index:
            r.index = index
        if always_unzip:
            r.zip_safe = not always_unzip
        r.executable = executable
        if path:
            r.eggs_caches = path
        if not versions:
            versions = buildout.get('versions', {})
        r.inst = zc.buildout.easy_install.Installer(
            dest=None,
            index=r.index,
            links=r.find_links,
            executable=r.executable,
            always_unzip=r.zip_safe,
            newest = newest,
            versions = versions,
            use_dependency_links = use_dependency_links,
            path=r.eggs_caches,
            allow_hosts=allow_hosts,
        )
        reqs, working_set = r._install_requirements(specs, dest, working_set)
        return working_set
    from zc.buildout import easy_install
    easy_install.install = install

    # try to patch zc.recipe.egg
    try:
        from zc.recipe import egg, custom
        egg.Eggs = Egg
        custom.Custom = Egg
        egg.Scripts = Script
    except:
        pass



# vim:set et sts=4 ts=4 tw=80:

