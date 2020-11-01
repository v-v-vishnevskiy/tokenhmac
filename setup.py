import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "tokenhmac", "__init__.py")) as f:
    for line in f:
        if line.startswith("__version__ ="):
            _, _, version = line.partition("=")
            VERSION = version.strip(" \n'\"")
            break
    else:
        raise RuntimeError("Unable to read the version from tokenhmac/__init__.py")


with open(os.path.join(os.path.dirname(__file__), "README.md")) as f:
    readme = f.read()


setup(
    name="tokenhmac",
    version=VERSION,
    author="Valery Vishnevskiy",
    author_email="v.v.vishnevskiy@yandex.ru",
    url="https://github.com/v-v-vishnevskiy/tokenhmac",
    project_urls={"GitHub: repo": "https://github.com/v-v-vishnevskiy/tokenhmac"},
    description="Fast JWT",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=["Operating System :: Unix", "Programming Language :: Python", "Programming Language :: Python :: 3"],
    license="MIT",
    keywords=["jwt", "token", "HMAC", "HS256", "HS384", "HS512", "encryption"],
    packages=["tokenhmac"],
    provides=["tokenhmac"],
)
