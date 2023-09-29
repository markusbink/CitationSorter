from setuptools import setup, find_packages

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name="citation_sorter",
    version="0.3.2",
    description=(
        "CitationSorter is a Python package for sorting and organizing citations in LaTeX documents."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/markusbink/latex-citation-sorter",
    packages=find_packages(),
    install_requires=[
        "argparse",
    ],
    entry_points={
        'console_scripts': [
            'citation_sorter=citation_sorter.citation_sorter:main'
        ]
    },
)
