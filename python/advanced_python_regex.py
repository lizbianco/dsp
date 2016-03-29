# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 11:02:55 2016

@author: EBianco
"""
#import necessary libraries
import csv
import string
import collections

#Create lists
LofD = []
Names = []
Degrees = []
Titles = []
Emails = []

#Load Data
with open('faculty.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            LofD.append(row)
            
def FillList (listname, key):
    for row in LofD:
        listname.append(row[key])
        
FillList(Names, 'name')
FillList(Degrees, ' degree')
FillList(Titles, ' title')
FillList(Emails, ' email')


#Q1
CleanDegrees = []
for i in Degrees:
    if i != '0': 
        for x in i.split():
            CleanDegrees.append(x)
CleanDegrees = [''.join(c for c in s if c not in string.punctuation)for s in CleanDegrees]
    
degreetally = collections.Counter(CleanDegrees)
print (degreetally)
print (len(degreetally))

#Q2
CleanTitles =[]
for i in Titles:
    if i == 'Assistant Professor is Biostatistics':
        CleanTitles.append('Assistant Professor of Biostatistics')
    else:
        CleanTitles.append(i)
print(CleanTitles)
        
titletally = collections.Counter(CleanTitles)
print (titletally)
print (len(titletally))

#Q3
print (Emails)

#Q4
Domains = []
for i in Emails:
    Domains.append(i.split('@')[1])

domaintally = collections.Counter(Domains)
domainlist = list(domaintally.keys()) 

print (domainlist)
print (len(domainlist))
    