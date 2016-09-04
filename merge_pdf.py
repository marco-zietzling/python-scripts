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

# iterate over files and append them
for file in files:
	print("processing " + file)
	input = open(working_directory + "\\" + file, "rb")
	merger.append(input)

# write output to new file
output = open(working_directory + "\\output.pdf","wb")
merger.write(output)
output.close()
