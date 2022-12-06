from io import StringIO
from pdfminer import *
# from pdfminer.converter import Textconverter
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfmminer.pdfpage import PDFpage
# from pdfminer.pdfparse import PDFparser


def convert_pdf(filepath):
    output_string = StringIO()
    with open(file_path, 'rb') as in_file
        parser = PDFParser(in_file)
        file = PDFDocument(parser)
        rs

#extract data from a pdf file using the pdfminer module in python.
#extract specific headers in pdf files and return it structurally in another file.
#extract table of content in pdf files and return it structurally in another file.