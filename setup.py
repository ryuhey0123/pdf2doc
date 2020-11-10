import codecs
import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()


required = [
    "pip>=18.0",
    "setuptools>=36.2.1",
    "pypdf2",
    "reportlab",
    "click",
    "crayons",
    "send2trash",
]

setup(
    name="pdf2doc",
    version="__version__",
    description="Make paged document by PDFs.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Ryuhei Fujita",
    packages=find_packages(exclude=["tests", "tests.*"]),
    entry_points={
        "console_scripts": [
            "pdf2doc = pdf2doc:cli",
        ]
    },
    install_requires=required,
    license="MIT"
)
