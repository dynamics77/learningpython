# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:45:41 2015

"""

#import pandas library
#used in the end to write csv format output

import pandas as pd

#initialize 
#empty list and dictionary

lst=[]
counts=dict()

#read lines one by one from the file.
#lower text
#remove punctuation and numbers
#strip extra space

fname=open("stou.txt")
for line in fname:
    words=line.split()
    if len(words)==0:continue
    line=line.rstrip()
    line=line.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~0123456789':
        line = line.replace(ch, ' ')
    line=line.split()  

#create dictionary of letters   
    for word in line:
        word.split()
#        print(word)
        for letter in word:
            counts[letter]=counts.get(letter,0)+1
#        print(counts)
    
for key,value in counts.items():
    lst.append((value,key))
    lst.sort()
    lst.sort(reverse=True)
#print(lst)

#convert list to data frame 
#then write dataframe to the csv file

df=pd.DataFrame(lst[:])
df.to_csv("letters_freq.csv", index=False)


