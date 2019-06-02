li=[1,2,4,2,1,4,3,2,3,1]
ll=[]
print li.count(1)
for i in range(0,len(li)-1):
    ll.append((li.count(li[i]),li[i]))
ll=sorted(set(ll),reverse=True)
print ll
