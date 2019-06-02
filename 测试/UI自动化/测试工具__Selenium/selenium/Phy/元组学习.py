#coding=UTF-8
import random
import random
list=[]
s=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j<>k:
                list.append(str(i)+str(j)+str(k))
                s=s+1
print len(list)
print s
if len(list)==s:
    print "是相等的！"
else:
    print "不相等！"
print list[random.randrange(1,len(list))]


import math
for n in range(1,1):
    i=math.sqrt(n+100)
    print i
    j=math.sqrt(n+268)
    print j
    if i/2.0==int(i/2) and j/2.0==int(j/2):
        print n
        break
 
import time
#print help(time.strftime)
print time.strftime("%Y")



list=[90,19,8,99,87,45,109]
list.sort()
print u"sort排序输出：",list
list=[90,19,8,99,87,45,109]
i=len(list)
for b in range(1,i):
    i=i-1
    for a in range(0,i):
        if list[a+1]<list[a]:
            temp=list[a+1]
            list[a+1]=list[a] 
            list[a]=temp
print u"冒泡排序输出：",list




print '*'*10
for i in range(5):
    print "*    *"
print '*'*10



import sys
#sys.stdout.write(chr(1))





temp=0#正常产仔的兔子
temp1=0#剩余一个月产仔的兔子
temp2=1#剩余2个月产仔的兔子
m=12#int(raw_input(u"请输入月份："))
for i in range(1,m+1):
    temp=temp+temp1
    temp22=temp2
    temp2=temp
    temp1=temp22
print "24个月后的兔子数量：",temp+temp1+temp2

f1=1
f2=1
for i in range(1,24):   
    #print "%12d%12d"%(f1,f1)
    if (i%2)==0:
        print ''
    f1=f1+f2
    f2=f1+f2

for  i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            if i**3+j**3+k**3==int(str(i)+str(j)+str(k)):
                print int(str(i)+str(j)+str(k))

import sys
from sys import stdout
n=45
print '数值：n=%d'%n
list=[]
for i in range(2,n+1):
    while n!=0:
        if n%i==0:
            list.append(str(i))
            sys.stdout.write(str(i))
            sys.stdout.write("*")
            n=n/i
        else:
            break
        print "%d"%n
for i in range(0,len(list)):
    if i<len(list)-1:
        sys.stdout.write(list[i]+"*")
    else:
        sys.stdout.write(list[i])

h=100
sum=0
for i in range(1,11):
    if i==1:
        print ''
        sum=sum+h
    h=h/2.0
    sum=sum+2*h
print h
print sum




            
