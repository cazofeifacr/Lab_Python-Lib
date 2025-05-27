from setuptools import find_packages, setup


setup(
    name="my_hw",
    version="0.1",
    packages=find_packages(),
    entry_points={"console_scripts": ["hola-mundo=src.main:hola_mundo"]},
)
