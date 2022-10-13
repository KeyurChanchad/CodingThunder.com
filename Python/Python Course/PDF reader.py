# Import the PyPDF2 and pyttx3 modules.
# Open the PDF file.
# Use PdfFileReader() to read the PDF. We just have to give the path of the PDF as the argument.
# Use the getPage() method to select the page to be read.
# Extract the text from the page using extractText().
# Instantiate a pyttx3 object.
# Use the say() and runwait() methods to speak out the text.

# importing the modules
import PyPDF2
import pyttsx3

# path of the PDF file
path = open("my.pdf", 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)

# the page with which you want to start
# this will read the page of 25th page.
from_page = pdfReader.getPage(2)

# extracting the text from the PDF
text = from_page.extractText()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
