#!/usr/bin/env python

from setuptools import setup, find_packages
import os


def strip_comments(line):
    return line.split('#', 1)[0].strip()


def read_requirements(*file_path):
    requirements_file = open(os.path.join(os.getcwd(), *file_path))
    return list(filter(None, [strip_comments(line) for line in requirements_file.readlines()]))


setup(name='pyseed',
      version='1.0',
      py_modules=['pyseed'],
      description='Seed Python Project',
      author='Roger',
      author_email='studyRoger@hotmail.com',
      #url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(),
      install_requires=read_requirements('requirements.txt'),
      )

