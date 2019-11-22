import tkinter
import traceback
import sys
relay = 1#0:抛出错误，终止脚本;1:重放代码;2:跳过出错代码

'''
    主要是写一个装饰函数，使脚本可以(重放、终止、跳过)  
'''
    
#装饰函数，使脚本可以(重放、终止、跳过)
def relay_entrace(func,check_element=False):
    def decorator(*args,**kwargs):
        #元素定位成功，执行内层方法    
        try:
            if func.__name__=='__init__':
                print(func.__name__)
                #print(dir(args[0]))
                func(*args,**kwargs)
            elif 'check_init' in dir(args[0]) or str(args[0]).find('object')==-1:
                print(func.__name__)
                if func.__name__=='__find_element__':
                    log("定位错误，args[0].locator")
                #print(args[0].check_init)
                if check_element:
                    if args[0].find_element():
                       return func(*args,**kwargs)
                else:
                    return func(*args,**kwargs)   
                             
        except Exception as e:
            #判断对象是不是实例，如果是执行实例方法，如果不是执行非实例方法
            if str(args[0]).find('object')!=-1:
                instance=args[0]
                args=args[1:]
                name=func.__name__
            else:
                instance=None
                args=args
                name=func.__qualname__
            detail_error="traceback.format_exc:\n%s"%traceback.format_exc()     
            error=str(locals()['func']).split(" ")[1]+"："+repr(e)
            next_step(instance,name,error,detail_error,*args,**kwargs)
    return decorator


#辅助函数，我们这里只应用于上方relay_entrace()函数中，判断relay_entrace()中下一步走向
def next_step(instance,name,error,detail_error,*args,**kwargs):
    '''
    描述：
        辅助函数，webelement_entrace元素出错装饰器
    参数：
        --instance：实例的名称
        --name：调用的函数名称
        --error：错误信息概要
        --detail_error：详细错误信息
        --*args：错误函数所需的参数变量集（有 传参数名）
        --**kwargs：错误函数所需的参数变量集（未传参数名）
    '''
    temp_relay=relay
    if temp_relay==2:
        print("跳过操作，错误信息："+error)
    elif temp_relay==1: 
        temp_relay=pop_up_box(error)
        if int(temp_relay)==1:
            print("重新执行，错误信息："+detail_error)
            if instance:             
                getattr(instance,name)(*args,**kwargs)
            else:
                eval(name)(*args,**kwargs)
        elif int(temp_relay)==2:
            print("跳过操作，错误信息："+error)
        else:
            print("停止执行，错误信息："+error)
            sys.exit()
    else:
        print("停止执行，错误信息："+error)
        sys.exit()

# 弹出一个窗口，根据不同的操作返回不同的数据
def pop_up_box(pop_text):
    def skip():
        var.set(2)
        root.destroy()

    def retry():
        var.set(1)
        root.destroy()

    def stop():
        var.set(0)
        root.destroy()

    root = tkinter.Tk()#窗口
    root.title("错误提示！")#窗口标题
    root.geometry("550x200")#设置窗口大小

    l1 = tkinter.Label(root,justify="left",text=content(pop_text))
    l1.pack()
    var = tkinter.StringVar()
    var.set("")
    btn1 = tkinter.Button(root, text="跳过", command=skip)
    btn2 = tkinter.Button(root, text="重试", command=retry)
    btn3 = tkinter.Button(root, text="停止", command=stop)
    btn3.pack(side='right')
    btn2.pack(side='right')
    btn1.pack(side='right')
    root.mainloop()
    return var.get()



#内容换行，pop_up_box()弹框异常信息打印专用，如有其它需要，请修改
def content(mycontent):
    mycontent="       "+mycontent
    for i in range(0,10):
        if i==0:
            text="错误信息："
        if len(mycontent)!=0:
            text=text+"\n"+mycontent[0:70]
            mycontent=mycontent[50:len(mycontent)]
        else:
            text=text+"\n       详细错误信息请见：日志目录"
            return text
            break


class test:
    @relay_entrace
    def __init__(self):       
        raise ImportError("__init__错误")
        self.check_init = True
        


    @relay_entrace
    def test_01(self):
        raise ImportError("导入的包是错误的！")

    @relay_entrace
    def test_02(self):
        raise ImportError("导入的包是错误的2！")

if __name__=='__main__':
    #pop_up_box('长时间的错误你知道吗，这是一个很坑爹的结果')
    test().test_01()
    test().test_02()