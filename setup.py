from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-idatasetform_bug',
	version=version,
	description="just a demo",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Hendrik Bunke',
	author_email='h.bunke@zbw.eu',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.idatasetform_bug'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	# myplugin=ckanext.idatasetform_bug:PluginClass
    idatasetform_bug=ckanext.idatasetform_bug.plugin:ExampleIDatasetFormPlugin
	""",
)
