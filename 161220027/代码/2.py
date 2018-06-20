# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 19:54:40 2018

@author: Lenovo
"""

n=int(input())
temp=input()
templist=temp.strip(" ").split(" ")
a=[]
for i in templist:
    tempint=int(i)
    a.append(tempint)

#old
    
l=[[],[],[]]
for i in range(n):
   l[i%3].append(a[i])

waittotal=0
time=[0]*3
for i in range(3):
    for j in range(len(l[i])):
        waittotal+=l[i][j]*(len(l[i])-j-1)# +=
        time[i]+=l[i][j]
        
timetotal=max(time)

print(waittotal,timetotal)

#new
time=0
totalwait=0
count=0
vac=[0]*3
while count!=n:
    #print(totalwait)
    if count>0:
        totalwait+=(n-count)
    time+=1
    for i in range(3):
        if vac[i]==0 :
            if count==n:
                break
            vac[i]=a[count]
            count+=1
        vac[i]-=1

time+=max(vac)
print(totalwait,time) #变量的一致性呀，哎呦喂 time 和 totalwait 都错了呀~