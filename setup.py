import os
from codecs import open

from setuptools import setup
from setuptools import find_packages


HERE = os.path.abspath(os.path.dirname(__file__))
PATH_VERSION = os.path.join(HERE, 'destijl', '__version__.py')


about = {}
with open(PATH_VERSION, 'r', 'utf-8') as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    packages=find_packages(
        include=[
            'destijl',
        ],
    ),
    install_requires=[
        'matplotlib>=3.3.2',
    ],
)
