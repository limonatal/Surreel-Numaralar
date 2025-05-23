import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setup(
    name="Sürreel Sayılar Paketi",
    version="0.0.2",
    author="limonatal, Nurullah Gümüş",
    author_email="limonatal@proton.me,gumus.mnur@outlook.com",
    description="Python package for operating over surreal numbers",
    long_description="This package eveloped to make it easier to work on surreal numbers; aritmatic and logic operations over surreal numbers such as comparing, adding and multiplication functionality implemented.",
    long_description_content_type="text/markdown",
    url="https://github.com/silverdevelopper/SurrealNum",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package= ['Surreel-Numaralar'],
    python_requires='>=3.8',
)
