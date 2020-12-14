#
#PURPOSE    : To Extract Text from PDF to the Excel.Comes in Handy when u are asked to €Go through a Large Number of the PDF Files and Respond to it.
#DATE       : 14-DEC-2020
#AUTHOR     : prakashvel.periyannan@gmail.com
#REFERENCE  :https://github.com/pdfminer/pdfminer.six
#           :https://www.journaldev.com/16140/python-system-command-os-subprocess-call
#           :https://pdfminersix.readthedocs.io/en/latest/reference/commandline.html#api-pdf2txt


#STEP 1:Please Use the Below step to convert the file  
# Use command-line interface to extract text from pdf:
# C:\Python3.8\Scripts>python pdf2txt.py samples/simple1.pdf

import subprocess
#python C:\Python3.8\Scripts\pdf2txt.py C:\sample.pdf
cmd = "python C:\\Python3.8\\Scripts\\pdf2txt.py C:\\sample.pdf --outfile C:\\sample.txt"

returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
print('Text Present in PDF', returned_value)

#
#cmd = "python C:\\Python3.8\\Scripts\\pdf2txt.py C:\\sample.pdf"
#

# returns output as byte string
#returned_output = subprocess.check_output(cmd)

# using decode() function to convert byte string to string
# print('Text Present in PDF:', returned_output.decode("utf-8"))