# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 06:50:42 2018

@author: Lenovo
"""
sale=[]
buy=[]

price_t=[]
price=[]

buytotal=0
saletotal=0
feetotal=0
m=int(input())
for i in range(m):
    temp=input()
    l=temp.split(" ")
    tempflag=int(l[2])
    if tempflag==1:
        buy.append((int(l[0]),int(l[1])))
    else:
        sale.append((int(l[0]),int(l[1])))

n=int(input())
for i in range(n):
    temp=input()
    l=temp.split(" ")
    price_t.append(int(l[0]))
    price.append(int (l[1]))
    
#print(sale,buy,price,price_t)

for i in buy:
    t=i[0]
    p=0
    j=0
    fee=0
    for j in price_t:
        if j>=t:
            break
    if j==t:
        p=price[price_t.index(j)]
    else:
        p=price[price_t.index(j)-1]
    
    volume=p*i[1]*100
    buytotal+=volume
    fee1=volume*0.002
    if fee1<5:
        fee1=5
    fee+=fee1
    fee+=int(i[1]*100/1000) #此处按照向下取整计算
    fee+=1
    feetotal+=fee

for i in sale:
    t=i[0]
    p=0
    j=0
    fee=0
    for j in price_t:
        if j>=t:
            break
    if j==t:
        p=price[price_t.index(j)]
    else:
        p=price[price_t.index(j)-1]
    
    volume=p*i[1]*100
    saletotal+=volume
    fee1=volume*0.002
    if fee1<5:
        fee1=5
    fee+=fee1
    fee+=int(i[1]*100/1000) #此处按照向下取整计算
    fee+=1
    fee+=volume*0.001
    feetotal+=fee
    
print(saletotal, buytotal,feetotal)
print(round(saletotal-buytotal-feetotal,2))
    