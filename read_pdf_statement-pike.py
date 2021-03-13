#import textract
#text = textract.process('/Users/stephen/Documents/Stephen/BankStatements/Smile/Statment36a.pdf', method='pdfminer')
#print(text.)

import pikepdf
#my_pdf = pikepdf.Pdf.open('test.pdf')

# creating a pdf file object 
pdfFileObj = pikepdf.Pdf.open('/Users/stephen/Documents/Stephen/BankStatements/Smile/Statment36a.pdf', 'rb') 

# creating a pdf reader object 
#pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# Name is on the 1st page of th efile.
# creating a page object 
pageObj = pdfReader.getPage(0) 
# extracting text from page 
#Write all the data to a list 

AllDataTab = pageObj.extractText()
# closing the pdf file object, not needed any more
pdfFileObj.close() 

 #Split the file on commers. While this does not create a good split is it a simple start to create lines for each record
AllDataTab = AllDataTab.split(",")

#Define data block as the 2nd line and the line which contains the string Statement closing balance
# define the end of data block
EOB=0
PreviousLine=["BlankLine"]
# loop throug data to find the end index 
for index, line in enumerate(AllDataTab):
    PreviousLine.append(line[0:5])
    #Dont process the first line
    if index == "0":
        continue
    elif "Statement closing balance" in line:
        EOB = index
        break
    else:
        print("line ",index, line[6:-2].replace("\n"," "),line[-2:]+PreviousLine[index])
#pp

#print(procd)
#print(output[1])

#print("line 1: ", AllDataTab[1][6:-2].replace("\n"," "))
#print("line 1: ", AllDataTab[1])

#for place, line in enumerate(AllDataTab):


#print("line 2: ",OutputTab[1].replace("\n"," "))
#print("Line 3: ",OutputTab[2].replace("\n"," "))


#for index, line in enumerate(OutputTab):
#    if "Statement closing balance" in line:
#        break
    

#print(index -1, OutputTab[index -1])
#print(index, OutputTab[index])

