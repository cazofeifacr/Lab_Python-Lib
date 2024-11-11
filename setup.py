from setuptools import setup, find_packages

setup(
    name="my_hw",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "hola-mundo=src.main:hola_mundo"
        ]
    },
)
