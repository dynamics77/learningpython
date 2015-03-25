# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:46:41 2015

"""

#iteration on string
leta=0
letc=0
letg=0
lett=0
line='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
#words=line.split()
for word in line:
    if word=="A":
      leta=leta+1
    elif word=="T":
      lett=lett+1
    elif word=="C":
        letc=letc+1
    elif word=="G":
        letg=letg+1
print("G:",letg,"C:",letc,"A:",leta,"T:",lett)   

#same thing but by list method 
leta=0
letc=0
letg=0
lett=0
lst=[]
line='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
for word in line:
    lst.append(word)
for let in lst:
    if let=="A":
     leta=leta+1
    elif let=="C":
     letc=letc+1
    elif let=="G":
     letg=letg+1
    elif let=="T":
        lett=lett+1
print("G:",letg,"C:",letc,"A:",leta,"T:",lett)

#now by dictionary method
counts=dict()
line='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
for word in line:
    if word not in counts:
        counts[word]=1
    else:
        counts[word] +=1
print(counts)       

#even more elegant way
counts=dict()
line='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
for word in line:
     counts[word] = counts.get(word,0) + 1
print(counts)
