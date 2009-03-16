from setuptools import setup, find_packages
import os

version = '1.0'

entry_point = 'buildout.minitagificator:install'
entry_points = {"zc.buildout.extension": ["default = %s" % entry_point]} 

setup(name='buildout.minitagificator',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Mathieu Pasquet',
      author_email='kiorky@cryptelium.net',
      url='http://svn.plone.org/svn/plone/plone.app.example',
      license='GPL',
      packages = find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['buildout', 'buildout.minitagificator'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zc.buildout',
          'minitage.recipe',
          'buildout.eggtractor',
          # -*- Extra requirements: -*-
      ],

      extras_require={'test': ['ZopeSkel', 'IPython', 'zope.testing', 'mocker']},
      entry_points= entry_points,
      )

