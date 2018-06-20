# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 20:46:50 2018

@author: Lenovo
"""

oprs=['+','-','*','/','(',')']
oprs1=['+','-','*','/']
pr={'+':1,'-':1,'*':2,'/':2}
def str2list(exps):
    #print(1)
    expl=[]
    num=0
    if_num=False
    for i in exps:
        #print(expl,if_num)
        #print(i)
        if i in oprs:
            if if_num:
                expl.append(num)
            expl.append(i)
            num=0
            if_num=False
        else:
            if_num=True
            #print(num,i)
            num=num*10+int(i)
    if if_num:
        expl.append(num)
    return expl

def computeOp(a,op,b):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        assert b!=0, "Invalid input."
        return a/b

def mid2front(expl):
    s1=[]
    s2=[]
    for i in expl:
        if type(i)==int:
            s2.append(i)
        elif i in oprs1:
            Flag=True
            while Flag:
                if len(s1)==0 or s1[len(s1)-1]==')':
                    s1.append(i)
                    Flag=False #表示已经放入 栈内
                elif pr[i]>=pr[s1[len(s1)-1]]:
                    s1.append(i)
                    Flag=False
                else:
                   temp=s1.pop()
                   s2.append(temp)
        else:
            if i=='(':
                temp=s1.pop()
                while temp!=')':
                    #print(s1,s2)
                    s2.append(temp)
                    temp=s1.pop()
            else:
                s1.append(')')
                
    while len(s1)!=0:
        temp=s1.pop()
        s2.append(temp)
    
    res=[]
    while len(s2)!=0:
        temp=s2.pop()
        res.append(temp)
    return res
                    
def compute(expf):
    s2=[]
    expfr=expf[::-1]
    for i in expfr:
        if type(i)==int:
            s2.append(i)
        else:
            opt=i
            a=s2.pop()
            b=s2.pop()
            temp=computeOp(a,opt,b)
            s2.append(temp)
            #print(s2)
    return s2[0]
            
if __name__ == '__main__':
    exps=input()
    expl=str2list(exps)
    exp=expl[::-1].copy()
    expf=mid2front(exp)
    expfs=''
    for i in expf:
        expfs+=str(i)
    print(expfs)
    print(compute(expf))