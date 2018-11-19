from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='AWSEnums',
    version='0.0.1.dev11',

    description='Python module that contains a list of enums useful for your applications.',
    long_description=long_description,

    url='https://github.com/SchibstedSpain/AWSEnums',

    author='Schibsted Spain',
    author_email='ferran.grau@scmspain.com',

    license='MIT',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='AWS enums',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['boto3'],
)
