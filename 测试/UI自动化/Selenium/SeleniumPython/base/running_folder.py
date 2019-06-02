import os,shutil,sys,multiprocessing
sys.path.append("..")
from base.get_config import MyConfig as myconfig
pid=multiprocessing.current_process().pid#获取pid进程编号
folderpath=myconfig("project","project_path").value+myconfig("project","data_path").value


def folder_create(path=None):
	if path:
		path=path
	else:
		path=folderpath+"/"+"testsuite-pid-"+str(pid)

	
	if os.path.exists(path)==False:
		os.mkdir(path)
	return path


def folder_clear(path=folderpath):
	path=os.path.abspath(path)	
	# print(path)
	# print(path.split("\\")[len(path.split("\\"))-1])
	print("目录名称",os.path.dirname(path))
	if path.split("\\")[len(path.split("\\"))-1]=="testsuite_tempdata":
		for root,dirs,filename in os.walk(path):
			print(str(dirs)+"||"+str(filename))
			for dir in dirs:
				if dir!="testsuite_debug":
					shutil.rmtree(path+"/"+dir)		
	else:
		print("清空目录:"+str(path)+"下文件夹，谨慎操作！")


if __name__=="__main__":	
	print(folder_create(folderpath))
	folder_clear()

