# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:18:25 2020

@author: Lakshmi Priya
"""

# importing required modules 
import PyPDF2 
import re

pdfName='The_Living_World.pdf'

# creating a pdf file object 
pdfFileObj = open(pdfName, 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

text=''
for i in range(pdfReader.numPages):
    # creating a page object 
    pageObj = pdfReader.getPage(i) 
    
    # extracting text from page 
    text=text+pageObj.extractText()

# closing the pdf file object 
pdfFileObj.close() 

f=open('output.txt','w')

# output file formatting
rep="Aakash Educational Services Pvt. Ltd. - Regd. Office : Aakash Tower, 8, Pusa Road, New Delhi-110005 Ph.011-47623456"    
text = text.replace('\n', '').replace('\r', '').replace('The Living World', '')
text = re.sub(rep, "", text)
text = re.sub("[0-9]{10,}", "", text)
text = re.sub("(\d+\.)", r"\n\n\1", text)
text = re.sub('(\(\d+)', r'\n\1', text)
text=text.replace('Sol', '\nSol').replace('SECTION', '\nSECTION').replace('Objective Type Questions', '\nObjective Type Questions')

f.write(text)
f.close()