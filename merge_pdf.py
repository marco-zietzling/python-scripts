"""Merge several PDF files within a given directoy to a new file called 'output.pdf'.
The first argument defines the directory.
PDF files are merged according to alphabetical order.
Usage: python merge_pdf.py path/to/directoy/containing/pdf/files
"""

import os
import sys
import warnings
from PyPDF2 import PdfFileMerger


def is_valid_directory(argument):
    """Sanity check argument to be an existing directoy.
    """

    condition1 = argument is not None
    condition2 = os.path.isdir(argument)
    return condition1 and condition2


def merge_pdf_files_in_directory(directory):
    """Merge all PDF files from given directory to a new file called 'output.pdf'.
    """

    merger = PdfFileMerger()
    files = os.listdir(directory)

    # Iterate over files and append them (consider only PDF files).
    for file in files:
        if file.lower().endswith(".pdf"):
            print("processing " + file)
            inputfile = os.path.join(directory, file)
            inputfile = os.path.normcase(inputfile)
            source_pdf = open(inputfile, "rb")
            merger.append(source_pdf)

    # Write output to new file.
    outputfile = os.path.join(directory, "output.pdf")
    target_pdf = open(outputfile, "wb")
    merger.write(target_pdf)
    target_pdf.close()


# Ignore all warnings (e.g. PDF read warnings).
warnings.filterwarnings("ignore")

if is_valid_directory(sys.argv[1]):
    merge_pdf_files_in_directory(sys.argv[1])
