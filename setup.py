#!/usr/bin/env python
import os

from setuptools import find_packages, setup
import versioneer


versioneer.VCS = 'git'
versioneer.versionfile_source = 'cumulus/_version.py'
versioneer.versionfile_build = None
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = 'django-cumulus-'

setup(
    name = "django-cumulus",
    version = versioneer.get_version(),
    cmdclass = versioneer.get_cmdclass(),
    packages = find_packages(),
    install_requires = [

        "pyrax @ https://github.com/wearespindle/pyrax/tarball/6ae5717d2b82a16e214f9cde31b23628e7176b34"
    ],
    author = "Ferrix Hovi, Thomas Schreiber",
    license = "BSD",
    description = "An interface to python-swiftclient and rackspace cloudfiles API from Django.",
    long_description = open("README.rst").read(),
    url = "https://github.com/django-cumulus/django-cumulus/",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
