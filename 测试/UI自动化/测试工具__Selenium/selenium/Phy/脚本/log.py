#coding=UTF-8
def log(content):
    import os
    import time
    path="..\\log\\"
    filename=time.strftime('%Y%m%d')+'.html'
    filepath=path+filename
    print(path)
    file=open(filepath,'a')
    file.write("""<!DOCTYPE html><html><head><title></title></head><body><input id="input"></body></html>""")
    #file.write(time.strftime('%H%M%S')+":%s"%content+"\n")
    file.close
#循环调用5次
for i in range(1,2):
    log("第"+str(i)+"次测试结果；")
