sum=0
for i in range(1,101):
    i=i*(-1)**(i+1)
    sum=sum+i
print "1-2+3-4+.....100=%s"%sum
