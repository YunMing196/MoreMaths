# setup.py
from setuptools import setup, find_packages

setup(
    name="MoreMaths",
    author="MingZe",
    version="1.0.0",
    packages=find_packages(),
    package_data={'MoreMaths': ['*.py']},
    python_requires=">=3.7",
)
