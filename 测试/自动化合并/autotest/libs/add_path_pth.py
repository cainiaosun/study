import sys
import os

#需要维护的所有自定义路径
#print('args is:',sys.argv[0])
paths=[
    "F:\\PrivateSpace\\GIT\\学习\\study\\测试\自动化合并\\autotest",
    "F:\\PrivateSpace\\GIT\\学习\\study\\测试\自动化合并\\autotest\\po",
]
# print('file is :',os.path.dirname(__file__))
# print('getcwd is :',os.getcwd())
# curdir = os.path.abspath('.')
# print('. is :',curdir)
# print('curdir is :',os.path.abspath(os.path.curdir))
# print('name is:',os.path.basename(os.path.dirname(__file__)))


def add_path_pth(paths):
    #获取本执行脚本所在的路径，如果是libs目录下,那么把libs和libs下所有的目录添加到paths变量中
    filedir=os.path.dirname(__file__)
    if os.path.basename(filedir)=='libs':
        #print('go in!!!!!!!!!!!!')
        paths.append(filedir)
        for pardir,subdir,subfile in os.walk(filedir,True):
            #print(pardir)
            if pardir==filedir:
                for dirname in subdir:
                    if os.path.basename(dirname).find('__')==-1:
                        paths.append(pardir+'\\'+dirname)
    #print('paths is',paths)

    #将paths内的所有路径追加到'site-packages'包下的pth文件中，python会从pth文件下路径读取扩展包
    for path in sys.path:
        #遍历环境变量,读取到'site-packages'变量后，在目录下新建pth文件或在内容上追加自定义目录
        if path.endswith('site-packages') and path.find('AppData')==-1:
            print("site-packages路径：",path)
            mypath=path+'\\autotest.pth'
            #判断有无文件，如果没有，新建一个，并在首行写注释
            if os.path.exists(mypath)==False:
                with open(mypath, 'w', encoding='gbk') as fp:
                    fp.write('#自定义文件路径'+'\n')
            #只读模式打开文件，获取添加自定义路径前的pth文件内容
            with open(mypath, 'r', encoding='gbk') as fp:
                fp_str = fp.read()
                fp_tuple = fp_str.split("\n")
                print('添加前--path.pth is :',fp_tuple)
            #追加模式打开，如果添加的路径在pth文件中不存在，则添加一行
            with  open(mypath,'a',encoding='gbk') as fp:
                for path in paths:
                    if fp_tuple.count(path) == 0:
                        fp.write(path+"\n")
            #只读模式打开，再次获取pth文件内容，比对是否添加成功
            with open(mypath, 'r', encoding='gbk') as fp:
                fp_str = fp.read()
                fp_tuple = fp_str.split("\n")
                print('添加后--path.pth is :', fp_tuple)

def delete_file_pth(filepth):
    for path in sys.path:
        #遍历环境变量,读取到'site-packages'变量后，删除目录下的autotest.pth文件
        if path.endswith('site-packages') and path.find('AppData')==-1:
            print("site-packages路径：",path)
            mypath=path+'/'+filepth
            print('mypath is',mypath)
            #判断有无文件，如果有，那么删除掉
            if os.path.exists(mypath):
                os.remove(mypath)


#执行方法,添加自定义路径到pth文件中
if __name__=='__main__':
    delete_file_pth('autotest.pth')
    add_path_pth(paths)