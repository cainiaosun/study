import os,shutil,sys,multiprocessing
pid=multiprocessing.current_process().pid

def folder_create(pid,name="testsuite"):
	path="./testsuite_tempdata/"+name+"-pid-"+str(pid)
	if os.path.exists(path)==False:
		os.mkdir(path)
		shutil.copyfile("./test.py",path+"/test_tem.py")
		file=open(path+"/test.yaml","w");file.close()	
		file=open(path+"/case.py","w");file.close()


def folder_clear(path):
	path=os.path.abspath(path)	
	# print(path)
	# print(path.split("\\")[len(path.split("\\"))-1])
	if path.split("\\")[len(path.split("\\"))-1]=="testsuite_tempdata":
		for root,dirs,filename in os.walk(path):
			print(str(dirs)+"||"+str(filename))
			for dir in dirs:
				shutil.rmtree(path+"/"+dir)		
	else:
		print("清空目录:"+str(path)+"下文件夹，谨慎操作！")



folder_create(pid)
#folder_clear("./testsuite_tempdata")

