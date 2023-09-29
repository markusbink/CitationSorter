# CitationSorter

**CitationSorter** is a Python package for sorting and organizing citations in LaTeX documents. It is designed to help you neatly arrange in-text citations within LaTeX files based on the author and publication year.

## Installation

You can install **CitationSorter** using pip:

```bash
pip install citation_sorter
```

## Usage

**CitationSorter** can be used both as a library and as a command-line tool.

### As a Library

You can use **CitationSorter** as a library in your Python scripts. Here's an example of how to use it:

```py
from citation_sorter import CitationSorter

# Create an instance of the CitationSorter class with input and output folders
sorter = CitationSorter()

# Process LaTeX files in the input folder and save the modified versions in the output folder
sorter.process_folder(input_folder='input_folder_path', output_folder='output_folder_path')
```

### As a Command-Line Tool

You can also use **CitationSorter** from the command line. After installing it, you can run it as follows:

```bash
citation_sorter input_folder output_folder
```

Replace **input_folder** with the path to the folder containing your LaTeX files and **output_folder** with the path where you want the modified files to be saved.

### LaTeX File Format

**CitationSorter** works with LaTeX files containing citation commands starting with \cite. It sorts the citations within these commands based on the author's name and publication year.

Example LaTeX citation command:

```latex
\cite{smith2023book, jones2022paper, brown2021article}
\cite[p.1]{smith2023book, jones2022paper, brown2021article}
\citet{smith2023book, jones2022paper, brown2021article}
\citep{smith2023book, jones2022paper, brown2021article}
```

# License

This project is licensed under the GPL-3.0 license. See the LICENSE file for details.
