# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 21:58:31 2014

Script to convert bibtex file to literature table in csv

@author: Rolf Groeneveld
"""

import csv
from bibtexparser.bparser import BibTexParser
from dicttoxml import dicttoxml
from operator import itemgetter

def selectDict(inpList,name):
    """
    Selects all dictionaries in a list of dictionaries where the author names
    include the name requested in name (str) AND where the reference type is 'article'
    """
    outObj = []
    for i in range(len(inpList)):
        if name in inpList[i]['author'] and inpList[i]['type']=='article':
            outObj.append(inpList[i])
    return(outObj)

def readFirstAuthor(inpList,num):
    """
    Reads name first author from the 'num'th dictionary in inpList (list of dictionaries)
    """
    author1 = ""
    x = inpList[num]['author']
    for j in x:
        if j != ',':
            author1+=j
        else:
            break
    return author1

def selectFieldsDict(inpList,fieldNames):
    """
    Selects from inpList (list of dictionaries) the fields specified in fieldNames (list of str)
    """
    outObj = []
    for i in range(len(inpList)):
        temp = {}
        for n in fieldNames:
            if n == 'author':
                author1 = readFirstAuthor(inpList,i)
                temp['author'] = author1
            else:
                if n in inpList[i]:
                    temp[n] = inpList[i][n]
                else:
                    temp[n] = 'blank'
        outObj.append(temp)
    return(outObj)

# Specify file name of bibtex file
litFileName = 'Example.bib'

# Specify author name to select
authorName = 'Kompas'

# Specify field names to be selected from the bibtext file
fieldnames = ['author','year','journal','quadrant','innovation','method',\
    'data','results','relevance']

# Parse data from bibtex file into object bp
with open(litFileName, 'r') as bibfile:
    bp = BibTexParser(bibfile.read())

# Get data from object bp as a list
# The result is a list of dictionaries
record_list = bp.get_entry_list()

# Select all references with author specified
dictSelection = selectDict(record_list,authorName)

# Select field names specified in references selected
fieldSelection = selectFieldsDict(dictSelection,fieldnames)

# Sort the selected data by year
fieldsSorted = sorted(fieldSelection, key=itemgetter('year'))

outputFile = open('output.csv','wb')
csvwriter = csv.DictWriter(outputFile, delimiter=',', fieldnames=fieldnames)
csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
for row in fieldsSorted:
     csvwriter.writerow(row)
outputFile.close()
