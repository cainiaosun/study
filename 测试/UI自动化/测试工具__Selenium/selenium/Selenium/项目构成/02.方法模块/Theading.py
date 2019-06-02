import threading,time
print(threading)
def time1(a,b):
	print(time.ctime())
	time.sleep(5)
	print("time1"+str(time.ctime()))
def time2(a,b):
	print(time.ctime())
	time.sleep(10)
	print("time2"+str(time.ctime()))

threadsk = []
t1=threading.Thread(target=time1,args=(1,2))
t2=threading.Thread(target=time1,args=(1,2))
t1.daemon=True
t1.start()


print("over")
time.sleep(15)
#apply(time1)


if sum(1+3)!=4:
	print("wrong!")