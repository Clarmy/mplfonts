import subprocess
import sys

try:
    import setuptools
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "setuptools"])
    import setuptools

import os
import codecs


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r", encoding="utf-8") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


FILE_PATH = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(FILE_PATH, "README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements_path = os.path.join(FILE_PATH, "requirements.txt")
with open(requirements_path, encoding="utf-8") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="mplfonts",
    version=get_version("mplfonts/__init__.py"),
    author="Wentao Li",
    author_email="clarmyleewt@outlook.com",
    description="Fonts manager for matplotlib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Clarmy/mplfonts",
    include_package_data=True,
    package_data={"": ["rc/matplotlibrc", "fonts/*"]},
    packages=setuptools.find_packages(),
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
    entry_points={"console_scripts": ["mplfonts = mplfonts.bin.cli:cli"]},
)
