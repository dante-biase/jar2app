# -*- coding: utf-8 -*-
from pathlib import Path
from setuptools import setup, find_packages

def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [str(path.parent) for path in Path(package).glob("**/__init__.py")]

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = "jar2app is an extremely simple, python based, command line tool to package JAR files into Mac OS applications"

setup(
    name="jar2app",
    version="1.0.0",
    description="command line tool to package JAR files into Mac OS applications",
    long_description=long_description,
    license="MIT",
    author="dante-biase",
    author_email="unknown",
    url="https://github.com/dante-biase/jar2app",
    packages=['', 'src'],
    package_data={
      '': ['*.ini', '*.ico', '*.png', '*.txt', '*.in', '*.md', '*.plist', '*.icns'],
      'resources/template.app/Contents': ['*.ini', '*.ico', '*.png', '*.txt', '*.in', '*.md', '*.plist', '*.icns'],
      'resources/template.app/Contents/MacOS': ['*.*'],
      'resources/template.app/Contents/Resources': ['*.ini', '*.ico', '*.png', '*.txt', '*.in', '*.md', '*.plist', '*.icns'],
      },
    python_requires='>=3.10',
    install_requires=[
      'click',
      'py2x',
      ],
    entry_points={"console_scripts": ["jar2app=jar2app:main"]},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ]
)
