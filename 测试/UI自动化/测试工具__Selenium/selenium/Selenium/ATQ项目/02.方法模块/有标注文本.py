#本模块是借用selenium的方法及模块封装的一套自己的元素识别与操作的模块，功能包括：
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
#作为定位元素出错后的后续操作判断：0：终止；1：暂停（提示错误，可重试）；2：跳过（继续执行下一步）。
relay=2
#浏览器对象，从测试测序中传值使用
driver=""

class find_element():
    #初始函数
    def __init__(self,locator="",relay=2):
        print("初始化")
        self.locator=locator
        self.relay=relay

     #常规元素定位函数
    def find_element(self):
        try:
            locator=self.locator
            return driver.find_element(locator[0], locator[1])
        except Exception as e:
            self.next_step("self.find_element",repr(e))

    #常规定位元素的清空操作
    def clear(self):
        try:
            from selenium import webdriver
            print("有执行clear？")
            self.find_element().clear()
        except Exception as e:
            print("clear进入异常？"+self.clear.__name__)
            print("self.clear()")
            print(self.locator)
            self.next_step("self.clear",repr(e))

    #常规定位元素的点击操作
    def click(self):
        try:
            from selenium import webdriver
            print("有执行click？")
            self.find_element().click()
        except Exception as e:
            print("click进入异常？"+self.click.__name__)
            self.next_step("self."+self.click.__name__,repr(e))       

    #常规定位元素的传值操作
    def send_keys(self,value):
        try:
            from selenium import webdriver
            print("有执行send_keys？")
            self.find_element().send_keys(value)
        except Exception as e:
            print("send_keys进入异常？"+self.send_keys.__name__)
            self.next_step("self.send_keys",repr(e),value)    
        

    #常规定位元素的传值操作
    def get_text(self):
        try:
            from selenium import webdriver
            return self.find_element().text()
        except Exception as e:
            self.next_step("self.get_text",repr(e))    

    def next_step(self,name,error,*parm):
        temp_relay=self.relay
        if temp_relay==1:
            print("跳过操作，错误信息："+error)
        elif temp_relay==2: 
            temp_relay=pop_up_box(error)
            print(temp_relay)
            if int(temp_relay)==2:
                print("重新执行，错误信息："+error)
                print("name是："+name)
                eval(name)(*parm)
                #self.clear()
            elif int(temp_relay)==1:
                print("跳过操作，错误信息："+error)
            else:
                print("停止执行，错误信息："+error)
                exit()
        else:
            print("停止执行，错误信息："+error)
            exit()



    # 弹出一个窗口并返回输入的值
def pop_up_box(content):
    import tkinter
    def skip():
        try:
            var.set(1)
            root.destroy()
        except:
            print("弹框关闭异常！")
    def retry():
        try:
            var.set(2)
            root.destroy()
        except:
            print("弹框关闭异常！")
    def stop():
        try:
            var.set(3)
            root.destroy()
        except:
            print("弹框关闭异常！")

    root = tkinter.Tk()#窗口
    root.title("错误提示！")#窗口标题
    root.geometry("700x100")#设置窗口大小

    l1 = tkinter.Label(root, text=content)
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


