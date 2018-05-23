#from distutils.core import setup
from setuptools import setup

long_description = open('README.md').read()

setup(
    name='Roll4Me',
    version='1.0',
    license='GPL3',
    author = 'Victor Caldas',
    author_email = 'caldas.victor@gmail.com',
    url = 'https://github.com/vcaldas/Roll4Me',
    download_url = 'https://github.com/vcaldas/Roll4Me',
    keywords = ['dnd', 'dice', 'wod'],
    description= 'A simple telegram dice bot using standard dice notation',
    long_description=long_description,
    scripts=[
        'bot',
    ]
)