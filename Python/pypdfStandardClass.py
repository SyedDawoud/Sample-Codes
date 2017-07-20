import PyPDF2
# Class to Process pdf Files
class PdfProcessor:

    def __init__(self):
        self.fileName=""
        self.pdfFile=None

    # Setting up the PDF file 
    def setAndOpenPdfFile(self,fileName):
        self.fileName=fileName
        self.pdfFile=PyPDF2.PdfFileReader(open(self.fileName,'rb'))

        # Page number start from 1-onwards
    def processOnlyOnePage(self,pageNumber):
        specificPage=self.pdfFile.getPage(pageNumber-1)
        reducedString=specificPage.extractText().replace('\n','')

        myArray=reducedString.split(' ')

        newString=""
        for x in myArray:
            if len(x) == 0:
                continue
            newString+=x+" "

        return newString.rstrip()

# Read the whole PDF File using the Above Process One Page Function only
    def readWholeDocument(self):
        data=""
            # Range will be 0=>total-1
        for currentPage in range(self.pdfFile.getNumPages()):
            # +1 is done as Pages Actual page start from 1-totalPageCount
            data+=self.processOnlyOnePage(currentPage+1)+"\n"

        return data.rstrip()
        

    
