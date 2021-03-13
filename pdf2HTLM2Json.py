

#/Users/stephen/Documents/Stephen/BankStatements/Smile/Statment36a.pdf
from lxml import html
import codecs
import os

# First convert the pdf to text/html
# You can skip this step if you already did it
os.system("/Users/paulcarter/anaconda3/bin/pdf2html /Users/stephen/Documents/Stephen/BankStatements/Smile/Statment36a.pdf >file.html")
# Open the file and read it
file = codecs.open("file.html", "r", "utf-8")
 # this is to break down the html string. 1st for row and column and then get the data from the next part.
def record_set(HTML_String):
   
    #The 1st split should create two parts. 
    Break_Line=HTML_String.split("<span")
    #1st for row and column 
    Row_Coloumn=Break_Line[0].split(";")
    # for item in Row_Coloumn:   
    #     if item[0:3]=="top":
    #         # take all char from : and remove the last two chars, should be pt. Top is the number of positions from the top of the file
    #         Row=item[4:-2]
    #     elif item[0:4]=="left":
    #         # take all chars from : and remove the last two chars, should be pt. Left is the number of chars from the left margin 
    #         Column=item[5:-7] #may be -7
    # Better way to do above with no loop
    Start_Position = Break_Line[0].find("top:")
    Start_Position += 4
    End_Position = Break_Line[0].find("pt",Start_Position)
    Row=int(Break_Line[0][Start_Position:End_Position])
    Start_Position = Break_Line[0].find("left:")
    Start_Position += 5
    End_Position = Break_Line[0].find("pt",Start_Position)
    Column=int(Break_Line[0][Start_Position:End_Position])

    #2nd  part get the data out of the BreakLine
    #Line_Data=Break_Line[1]
        #check need to find data between the chars > and <
    Start_Position = Break_Line[1].find(">")
    #want the string to star after the > char
    Start_Position = Start_Position + 1
    End_Position = Break_Line[1].find("<",Start_Position)
    Line_data = Break_Line[1][Start_Position:End_Position]
    Return_List=[Row,Column,Line_data]
    return Return_List

# Read in the data to add line numbers. The first row should contain the following data values: Date Description,Moneyout,Money in, Balance
def findFirstRow(No_Line_Data):
    Lines=No_Line_Data
    for NLD in Lines:
        if NLD[2]=='Date':
            First_Line=NLD[0]
        if NLD[2]=='Statement closing balance':
            Last_Line=NLD[0]
    return int(First_Line),int(Last_Line)

def reduceRows(List,First,Last):
    List_Of_Data = List
    New_List=[]
    for row in List_Of_Data:
        if First <=int(row[0]) <= Last:
            New_List.append(row) 
    return New_List
def sortLines(data_list, whichElement):
    l = len(data_list) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (data_list[j][whichElement] > data_list[j + 1][whichElement]): 
                tempo = data_list[j] 
                data_list[j]= data_list[j + 1] 
                data_list[j + 1]= tempo 
    return data_list 

def headerValue(dataBlock, lineNumber):
    firstLine = []
    for line in dataBlock:
        if lineNumber == line[0]:
            firstLine.append(line)
    return firstLine
data = file.read()
# We know we're dealing with html, let's load it
#html_file = html.fromstring(data)
Lines_Data = data.split("\n")
Line_Values=[]
NOL = 0
for line in Lines_Data:
    if line[0:2]=="<p":
        #bob=record_set(line)
        Line_Values.append(record_set(line))
        NOL +=1

#Find the start and end of the rows
Range_Of_line = findFirstRow(Line_Values)

# As it's an html object, we can use xpath to get the data we need
# In the following I get the text from <div><span>MY TEXT</span><div>
#extracted_data = html_file.xpath('//div//span/text()')
# It returns an array of elements, let's process it

#for elm in extracted_data:
    # Do things
file.close()
# for data in Line_Values:
#         print(data[2])
#print(Line_Values[0][1])
Begin=int(Range_Of_line[0])
print(Begin)
End=int(Range_Of_line[1])
print(End)
element = 0
AnotherList=reduceRows(Line_Values,Begin,End)
sortLines(AnotherList,element)
print(AnotherList)
line1=headerValue(AnotherList,Begin)
sortLines(line1,1)
print(line1)
rownum =0
for idx,lineNum in enumerate(AnotherList):
    print(lineNum[0],idx)
    if idx != 0:
        if lineNum[0] == lastValue:
            lastValue = lineNum[0]
        else:
            rownum +=1
    else:
        lastValue = lineNum[0]

    AnotherList[idx].append(rownum)    
    print(AnotherList[idx])

