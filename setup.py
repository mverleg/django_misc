# -*- coding: utf-8 -*-

"""
	Adapted from https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
"""

from setuptools import setup, find_packages


with open('requires.pip', 'r') as fh:
	requires = [package.split('# ')[0].strip() for package in fh.read().splitlines()
	    if package.strip() and not package.startswith('#')]

setup(
	name='misc',
	description='A lot of random utilities',
	long_description='',
	url='',
	author='Mark V',
	maintainer='(the author)',
	author_email='mdilligaf@gmail.com',
	license='',
	keywords=['django',],
	version='1.0',
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	install_requires=requires,
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: Implementation :: PyPy',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Private :: Do Not Upload By Accident',
	], requires=['django']
)
