#!/usr/bin/env python3
from setuptools import setup
import re


def getprop(prop):
	match = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open('pyanywhere/__init__.py').read())
	return match.group(1)

with open('README.md', 'r') as f:
	readme = f.read()


setup(
	name='pyanywhere',
	author='Dull Bananas',
	author_email='dull.bananas0@gmail.com',
	version=getprop('__version__'),
	description='Wrapper around the PythonAnywhere API with classes for consoles, webapps, etc.',
	long_description=readme,
	long_description_content_type='text/markdown',
	url='https://github.com/dullbananas/pyanywhere',
	license='MIT',
	
	packages=['pyanywhere'],
	install_requires=[
		'requests',
	],
	python_requires='>=3.6',
	
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3 :: Only',
		'Topic :: Internet',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
)
