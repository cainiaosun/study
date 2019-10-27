import sys
import os

#需要维护的所有自定义路径
paths=(
    "F:/GIT文件/study/测试/UI自动化/Selenium/SeleniumPython",
    "F:/GIT文件/study/测试/UI自动化/Selenium",
)

def add_path_pth(paths):
    for path in sys.path:
        #遍历环境变量,读取到'site-packages'变量后，在目录下新建pth文件或在内容上追加自定义目录
        if path.endswith('site-packages') and os.path.isdir(path):
            mypath=path+'\\mypath.pth'
            os.path.exists(mypath)
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
                print('添加后--fp_tuple is :', fp_tuple)

#执行方法
add_path_pth(paths)

