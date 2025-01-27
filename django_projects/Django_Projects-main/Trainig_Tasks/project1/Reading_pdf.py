import PyPDF2


pdfFileObj = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
print(pdfReader.numPages)
extra = (pageObj.extractText())
print(extra)


