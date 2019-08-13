import os,sys,shutil,multiprocessing
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
	path=os.path.abspath(path)#转换为绝对路径
	#print("目录名称",os.path.dirname(path))
	if path.split("\\")[len(path.split("\\"))-1]=="runningdata":#如果是runningdata目录，name操作删除
		for root,dirs,filename in os.walk(path,False):
			#print("-------------------------------------------------")
			#print(str(root),"||",str(dirs)+"||"+str(filename))
			for dir in dirs:
				if dir!="data_debug" and dir!="data_running" and root==path:
					shutil.rmtree(path+"/"+dir)
	else:
		print("清空目录:"+str(path)+"下文件夹，谨慎操作！")


if __name__=="__main__":
	print("创建了文件：",folder_create())
	print(folder_clear())