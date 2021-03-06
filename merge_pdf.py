"""Merge several PDF files within a given directoy to a new file called 'output.pdf'.
The first (and only) argument defines the directory.
PDF files are merged according to alphabetical order.
Usage: python merge_pdf.py path/to/directoy/containing/pdf/files
"""

import os
import sys
import warnings
from PyPDF2 import PdfFileMerger


def is_valid_dir(argument):
    """Sanity check argument to be an existing directoy.
    """

    arg_not_none = argument is not None
    arg_is_dir = os.path.isdir(argument)
    return arg_not_none and arg_is_dir


def merge_pdf_files_in_dir(directory):
    """Merge all PDF files from given directory to a new file called 'output.pdf'.
    """

    merger = PdfFileMerger()
    files = os.listdir(directory)
    files.sort()

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
    merger.close()


# Ignore all warnings (e.g. PDF read warnings).
warnings.filterwarnings("ignore")

if is_valid_dir(sys.argv[1]):
    merge_pdf_files_in_dir(sys.argv[1])
