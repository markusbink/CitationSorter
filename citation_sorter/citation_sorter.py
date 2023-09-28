import re
import os
import argparse
import logging


class CitationSorter:
    def __init__(self, input_folder, output_folder):
        """
        Initialize the CitationSorter.

        :param input_folder: The input folder path.
        :param output_folder: The output folder path.
        """
        self.input_folder = input_folder
        self.output_folder = output_folder

    def process_folder(self):
        """
        Process all LaTeX files in the input folder and save the modified versions in the output folder.
        """
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        for root, _, files in os.walk(self.input_folder):
            for file in files:
                if file.endswith(".tex"):
                    file_path = os.path.join(root, file)
                    self.process_file(file_path)

    def process_file(self, input_file):
        """
        Process a single LaTeX file and save the modified version in the output folder.

        :param input_file: The input file path.
        """
        with open(input_file, "r") as f:
            text = f.read()

        replaced_text = self.replace_citations(text)

        output_file = os.path.join(self.output_folder, os.path.basename(input_file))

        with open(output_file, "w") as f:
            f.write(replaced_text)

    def replace_citations(self, text):
        """
        Replace original citations in a LaTeX document with sorted citations.

        :param text: The LaTeX document text.
        :return: The modified LaTeX document text.
        """
        replaced_text = re.sub(
            r"\\cite.+?{.+?}", lambda match: self.sort_citations(match.group(0)), text
        )
        return replaced_text

    def sort_citations(self, raw_citation):
        """
        Sort citations in a LaTeX citation command alphabetically by author and then by year.

        :param raw_citation: The raw citation string.
        :return: The modified citation string.
        """
        match = re.search(r"(\\cite.+?){(.+?)}", raw_citation)
        citation_type, citations = match.groups()

        cites = [cite.strip() for cite in citations.split(",")]

        if len(cites) <= 1:
            return raw_citation

        sorted_citations = sorted(cites, key=self.get_author_year)
        sorted_citations_string = ",".join(sorted_citations)

        return f"{citation_type}{{{sorted_citations_string}}}"

    def get_author_year(self, cite):
        """
        Get the author and year from a citation.

        :param cite: The citation string.
        :return: A tuple containing author and year.
        """
        match = re.search(r"(\w+)(\d{4})\w+", cite)
        author, year = match.groups()
        return (author, int(year))


def main():
    parser = argparse.ArgumentParser(description="Replace citations in LaTeX files.")
    parser.add_argument("input_folder", help="Input folder path")
    parser.add_argument("output_folder", help="Output folder path")
    args = parser.parse_args()

    replacer = CitationSorter(args.input_folder, args.output_folder)
    replacer.process_folder()
    logging.info(f"Replaced texts saved to {args.output_folder}")


if __name__ == "__main__":
    main()
