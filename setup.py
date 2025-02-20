from setuptools import setup, find_packages
import pathlib

setup(
	name='genview',
	version='0.1',
	description='Gene-centric visualization tool for genomic sequences',
	url='https://github.com/EbmeyerSt/GEnView',
	author='Stefan Ebmeyer',

	packages=find_packages(),
	include_package_data=True,
	entry_points={
		'console_scripts': [
			'genview-makedb=genview_scripts.genview_create_db:main',
			'genview-visualize=genview_scripts.genview_visualize:main'],
		},
	zip_safe=False)
