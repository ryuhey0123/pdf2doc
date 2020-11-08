import codecs
import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()


setup(
    name="pdf2doc",
    version="1.0",
    description="Make paged document by PDFs.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Ryuhei Fujita",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pdf2doc = pdf2doc:cli",
        ]
    },
)
