from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument



def file1():
	file1 = open('pdffileD1.pdf', 'rb')
	parser = PDFParser(file1)
	doc = PDFDocument(parser)
	print("File 1 Extracted Meta Data: ", doc.info)

def file2():
        file2 = open('pdffileD2.pdf', 'rb')
        parser = PDFParser(file2)
        doc = PDFDocument(parser)
        print("File 2 Extracted Meta Data: ", doc.info)

file1()
file2()
