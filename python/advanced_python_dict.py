#import necessary libraries
import csv
import pprint
import collections
from collections import OrderedDict
from operator import itemgetter
#Create lists and dict
LofD = []


#Load Data
with open('faculty.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            LofD.append(row)
           
#Split name
names = []
for i in LofD:
    name = i['name']
    split = name.split(' ')
    l = len(split)    
    i['last name'] = split[l-1]
    if l == 2:
        i['first name'] = split[0]
    else:
        i['first name'] = ' '.join(split[:l-1])
    

#Q6
faculty_dict = {}
for i in LofD:
    k = i['last name']
    v = [i[' degree'], i[' title'],i [' email']]
    if not k in faculty_dict:
        faculty_dict[k] = v
    else:
        faculty_dict[k].append((v))
pp = pprint.PrettyPrinter(depth=6)
pp.pprint (faculty_dict)

#Q7
professor_dict = {}
for i in LofD:
    First = i['first name']
    Last = i['last name']
    v = [i[' degree'], i[' title'],i [' email']]
    professor_dict[First, Last]=v
pp = pprint.PrettyPrinter(depth=6)
pp.pprint (professor_dict)

#Q8
keys = list(professor_dict)
keys = (sorted(keys, key = lambda x: x[1]))
for k in keys:
    print(k, professor_dict[k])



