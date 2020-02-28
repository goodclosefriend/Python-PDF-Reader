  
import PyPDF2 as p2
#This is to insert your pdf file into the program
PDFfile = open("insert pdf file here .pdf", "rb")
#This will open the pdf file so it is able to read it

pdfread = p2.PdfFileReader(PDFfile)


# this is to get all of the data from each page onto a console line.


i = 0
while i <pdfread.getNumPages():
    pageinfo = pdfread.getPage(i)
    print(pageinfo.extractText())
    i = i + 1
#closes the pdf file
pdfread.close()
