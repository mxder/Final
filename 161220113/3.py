buynum=int(input())
time=[]
num=[]
buyelse=[]
for i in range(0,buynum):
    strlist=input().split()
    time.append(int(strlist[0]))
    num.append(int(strlist[1]))
    buyelse.append(int(strlist[2]))
pricechange=int(input())
time2=[]
price=[]
for i in range(0,pricechange):
    strlist=input().split()
    time2.append(int(strlist[0]))
    price.append(int(strlist[1]))
sum=0
for i in range(0,len(time)):
    if(buyelse[i]==1):
        pricenow=0
        for j in range(0,len(time2)+1):
            if(time[i]>=time2[j] and ((time[i]<time2[j+1]) or i==len(time2))):
                pricenow=price[j]
        yongjin=pricenow*100*num[i]*0.002
        if(yongjin<5):
            yongjin=5
        guohufei=int((100*num[i])/1000)
        tongxunfei=1
        money=pricenow*100*num[i]+yongjin+guohufei+tongxunfei
        sum=sum-money
    elif(buyelse[i]==2):
        pricenow=0
        for j in range(0,len(time2)):
            if(time[i]>=time2[j] and ((time[i]<time2[j+1]) or i==len(time2))):
                pricenow=price[j]
        yongjin=pricenow*100*num[i]*0.002
        if(yongjin<5):
            yongjin=5
        guohufei=int((100*num[i])/1000)
        tongxunfei=1
        money=pricenow*100*num[i]+yongjin+guohufei+tongxunfei
        yinhuashui=money*0.001
        sum=sum+money-yinhuashui
print(round(sum,2))
        