# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:00:28 2018

@author: Lenovo
"""

string=input()
list_s=string.split(" ")

n_list=[]

for i in list_s:
    n_list.append(int(i))

n_list.append(n_list[0]*n_list[1])
list_s.append(str(n_list[0]*n_list[1]))
list_len=[]
for i in list_s:
    list_len.append(len(i))
    
maxlen=0
for i in list_len:
    if i>maxlen:
        maxlen=i
        
list_l=[]
for i in list_s:
    space=' '*(maxlen-len(i))
    list_l.append(space+i)

print(list_l[0])
print(list_l[1])
print('-'*maxlen)
print(list_l[2])
    