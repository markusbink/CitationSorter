from setuptools import setup, find_packages

setup(
    name="citation_sorter",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "argparse",
        "re",
        "os",
    ],
)
