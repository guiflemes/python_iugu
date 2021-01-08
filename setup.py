from setuptools import find_packages
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from python_iugu.version import __version__

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'python_iugu'))

setup(
    name='python_iugu',
    packages=find_packages(),
    version=__version__,
    license='MIT',
    description='This provides Python REST APIs to create, process and manage payments on IUGU.',
    author='Guilherme Silva',
    author_email='guilherme.1995lemes@gmail.com',
    keywords=['iugu', 'rest', 'payment'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    install_requires=[
        "aiohttp~=3.7.3",
        "deserialize~=1.8.0",
        "setuptools~=51.1.1"
    ],
    setup_requires=[
        "aiohttp~=3.7.3",
        "deserialize~=1.8.0",
        "setuptools~=51.1.1"
    ],

)
