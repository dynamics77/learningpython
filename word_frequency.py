# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 23:38:26 2015

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

fname=open("stou.txt",'r')
for line in fname:
    words=line.split()
    if len(words)==0:continue
    line=line.rstrip()
    line=line.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~0123456789':
        line = line.replace(ch, ' ')
    line=line.split()  

#create dictionary of words   
    for word in line:
        counts[word]=counts.get(word,0)+1

# sort words by the frequency 
#of occurence in the dictionary 
        
for key,value in counts.items():
    lst.append((value,key))
    lst.sort()
    lst.sort(reverse=True)
#print(lst)  

#extract words with length more than 5
#reason is that I do not want most common words 
#"a", "the","or"  etc in the list

newlist=[]
for key,value in lst:
    if len(value) > 5:
     newlist.append((key,value))
#     print(value,key)
        
#convert list to data frame 
#then write dataframe to the csv file
        
df=pd.DataFrame(newlist[:50])
df.to_csv("words_freq.csv", index=False)
