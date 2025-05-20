from setuptools import setup, find_packages
import os

version = '2.4.30.dev0'

entry_point = 'buildout.minitagificator.minitagificator:install'
entry_points = {"zc.buildout.extension": ["default = %s" % entry_point]}

setup(name='buildout.minitagificator',
      version=version,
      description="A buildout extension to replace buildout part by minitage interesant ones sponsored by Makina Corpus",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("src", "buildout", "minitagificator", "minitagificator.txt")).read()+"\n"+
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Buildout",
          "Framework :: Plone",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='',
      author='Makina Corpus',
      author_email='freesoftware@makina-corpus.com',
      url='https://github.com/minitage/buildout.minitagificator',
      license='GPL',
      package_dir = {'': 'src'},
      packages = find_packages('src'),
      namespace_packages=['buildout', 'buildout.minitagificator'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zc.buildout',
          'minitage.recipe.egg >= 1.88',
          'minitage.recipe.cmmi',
          'minitage.recipe.scripts',
          'minitage.recipe.common',
          # -*- Extra requirements: -*-
      ],

      extras_require={'test': ['virtualenv',
                               'ZopeSkel',
                               'IPython',
                               'zope.testing',
                               'mocker',
                               'zc.recipe.egg',
                               'zc.recipe.cmmi'
                              ]
                     },
      entry_points= entry_points,
      )

