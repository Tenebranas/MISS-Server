import io
from io import BytesIO
from urllib.request import Request,urlopen
from PyPDF2 import PdfReader

def filepdf(file):
    importpdf = open(file, 'rb') #creates a pdf file object
    pdf = PdfReader(importpdf) #creates a pdf reader object

    return pdf

def urlpdf(url): #takes in url of pdf, returns a pdf python object
    info = urlopen(Request(url)).read() #send request to url -> open the info from the url/server -> read info
    usablebytes = io.BytesIO(info) #takes data from info & stores as usable bytes
    pdf = PdfReader(usablebytes) #read file using pdf reader & store file

    return pdf

def pdftext(pdf): #takes in pdf python object, returns text
    text = ''
    for i in range(len(pdf.pages)): #loops each page of pdf, .numPages = get page number
        page = pdf.pages[i] #.getPage = get a single page (page number = i)
        text += page.extract_text() #add the extracted text from each page to the entire text

    return text

def main(state):
    if state[0:5] == 'https' or state[0:4] == 'http': #if first 5 things of the string is "https"
        pdfreturn = urlpdf(state) #performs function "urlpdf"
        textreturn = pdftext(pdfreturn) #performs function "pdftext"
        return textreturn
    else: #otherwise
        pdfreturn = filepdf(state)
        textreturn = pdftext(pdfreturn)
        return textreturn