import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="slackpoint",
    version='1.0.0',
    url="https://github.com/nehakale8/slackpoint",

    author="Neha Kale",
    author_email="kaleneha997@gmail.com",

    description="Sets up the project automatically.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",

    packages=find_packages(exclude=('test',)),

    install_requires=['numpy', 'pytest'
                      ],
    dependency_links=[
    ],
    setup_requires=[
        'flask>=2.2.2',
        'pip>=20'
    ],
    python_requires='>=3.8',

    classifiers=[
        'Development Status :: 1 - Production',
        'Natural Language :: English',
        # 'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        "Operating System :: OS Independent"
    ],

)
