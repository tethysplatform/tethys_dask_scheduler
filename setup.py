"""
********************************************************************************
* Name: setup.py
* Authors: Nathan Swain, Tran H, Teva V
* Created On: 2018
* Copyright: AQUAVEO LLC
* License: BSD 2-Clause License
********************************************************************************
"""
import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

requires = []

version = '2.0.4'

setup(
    name='tethys_dask_scheduler',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    license='BSD 2-Clause License',
    description='A Dask scheduler with custom SchedulerPlugins to support integration with Tethys Platformt',
    long_description=README,
    url='http://tethysplatform.org/',
    author='Nathan Swain',
    author_email='nswain@aquaveo.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    entry_points={
        'console_scripts': ['tethys_ds=tethys_dask_scheduler:go', ],
    },
    install_requires=requires,
    extras_require={
        'tests': [
            'requests_mock',

        ],
        'docs': [
            'sphinx',
            'sphinx_rtd_theme',
            'sphinxcontrib-napoleon',
            'pbr',
        ]
    },
)
