import codecs
import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()


required = [
    "click==7.1.2",
    "colorama==0.4.4",
    "crayons==0.4.0",
    "pip==20.2.1",
    "PyPDF2==1.26.0",
    "Send2Trash==1.5.0",
    "setuptools==49.2.1",
    "wheel==0.35.1",
    "fpdf==1.7.2",
    "yaspin==1.2.0"
]

setup(
    name="pdf2doc",
    version="1.2.1",
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
