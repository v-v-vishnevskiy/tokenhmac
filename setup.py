import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "tokenhmac", "__init__.py")) as f:
    for line in f:
        if line.startswith("__version__ ="):
            _, _, version = line.partition("=")
            VERSION = version.strip(" \n'\"")
            break
    else:
        raise RuntimeError("Unable to read the version from tokenhmac/__init__.py")


setup(
    name="tokenhmac",
    version=VERSION,
    author="Valeriy Vishnevskiy",
    author_email="v.v.vishnevskiy@yandex.ru",
    license="as-is",
    packages=find_packages(),
    classifiers=["Operating System :: Unix", "Programming Language :: Python", "Programming Language :: Python :: 3"],
)
