# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:35:20 2018

@author: Lenovo
"""

import itertools

def form_st_ps_list(re2_ps,n_st):
    temp=itertools.combinations(re2_ps,n_st)
    st_ps_list=[]
    for i in temp:
        st_ps_list.append(i)
    return st_ps_list
        

if __name__ == '__main__':
   temp1=input()
   temp2=input()
   temp1=temp1.split(" ")
   n_res=int(temp1[0])
   n_st=int(temp1[1])
   temp2=temp2.strip(" ").split(" ")
   res_ps=[]
   for i in temp2:
       res_ps.append(int(i))
   #print(n_res,n_st,res_ps)
   st_ps_list=(form_st_ps_list(res_ps,n_st))
   sum_dist=[]
   for i in st_ps_list:
       dist=[]
       for j in res_ps:
           min=999999
           for k in i:
               if min>abs(j-k):
                   min=abs(j-k)
           dist.append(min)
       sum_d=sum(dist)
       #print(sum_d,dist)
       sum_dist.append(sum_d)
   Min=99999999
   for i in sum_dist:
       if i<Min:
           Min=i
    

   print(Min)
   
    