# merge several PDF files from a directoy to a new file called 'output.pdf'
# the first argument defines the directory
# PDF files are merged according to alphabetical order
# usage: python merge_pdf.py path/to/directoy/containing/pdf/files

import os
from PyPDF2 import PdfFileMerger
import sys
import warnings

# ignore all warnings (e.g. PDF read warnings)
warnings.filterwarnings("ignore")

# define the PDF merger
merger = PdfFileMerger()

# get the working directory and all files in it
working_directory = sys.argv[1]
files = os.listdir(working_directory)
# print(working_directory)
# print(files)

# iterate over files and append them (consider only PDF files)
for file in files:
    if file.lower().endswith(".pdf"):
        print("processing " + file)
        filepath = os.path.join(working_directory, file)
        filepath = os.path.normcase(filepath)
        input = open(filepath, "rb")
        merger.append(input)

# write output to new file
outputfile = os.path.join(working_directory, "output.pdf")
output = open(outputfile,"wb")
merger.write(output)
output.close()
