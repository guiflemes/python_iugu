try:
    from distutils.core import setup
except ImportError:
    from setuptools import setup

import os
import sys
from distutils.core import setup

from python_iugu.version import __version__

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'python_iugu'))

setup(
    name='python_iugu',
    packages=['python_iugu'],
    version=__version__,
    license='MIT',
    description='This provides Python REST APIs to create, process and manage payments on IUGU.',
    author='Guilherme Silva',
    author_email='guilherme.1995lemes@gmail.com',

    keywords=['iugu', 'rest', 'payment'],
    install_requires=[
        "aiodns",
        "aiohttp",
        "async-timeout",
        "attrs",
        "brotlipy",
        "cchardet",
        "certifi",
        "cffi",
        "chardet",
        "deserialize",
        "idna",
        "multidict",
        "pycares",
        "pycparser",
        "typing-extensions",
        "urllib3",
        "yarl",
    ],
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
)
