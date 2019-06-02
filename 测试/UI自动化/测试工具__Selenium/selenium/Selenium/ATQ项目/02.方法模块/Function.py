#本模块是借用selenium的方法及模块封装的一套自己的元素识别与操作的模块，功能包括：
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
sys.path.append(".//")
import 鼠标键盘事件 as event
#relay：错误处理选项：1.跳过；2.重新执行；3.停止。
relay=2
#浏览器对象，从测试测序中传值使用
driver=""

#定位操作操作的单个元素
class find_element():
    '''
    find_element()定位元素
    element()返回一个元素
    clear()清空元素
    click()点击元素
    js_click()通过js语句点击元素
    send_keys()向元素传值
    select()标准select选择框选择方法
    get_attribute()获取元素属性，包括text
    get_text()获取文本
    highlight()高亮元素
    set_attribute()设置元素属性值，包括text
    exist()元素显式等待
    focus()悬浮鼠标到元素
    left_click()单击左键
    double_click()双击左键
    click_and_hold()点击左键不放开
    right_click()单击右键
    '''

    #初始化函数
    def __init__(self,locator=""):
        """
        #初始化函数
        参数 locator：选择器，形式(By.ID)
        参数 relay：错误处理选项：1.跳过；2.重新执行；3.停止。
        """
        self.locator=locator
        self.relay=relay
        from selenium.webdriver.common.action_chains import ActionChains
        self.ActionChains=ActionChains

    #修饰器
    def entrace(fun):
        '''fun:解取被装饰函数的函数实例（注：这个fun存储的实例在其他地方使用，但是被调用时是直接调用
        不会再调用一次装饰函数）'''
        def decotor(*args,**kwargs):
            #*args:接取被装饰函数传参未带参数名的参数，如：function(1,2,c=5)中的1和2参数
            #**kwargs:接取被装饰函数传参带有参数名的参数，如：function(1,2,c=5)中的5参数
            try:
                return fun(*args,**kwargs)
            except Exception as e:
                #类的实例参数（注：类的实例参数可以在其他地方调用）
                instance=args[0]
                '''去除self(类的实例)后调用方法的剩余不参数名的参数（注：被装饰函数都是类的公有函数
                所以第一个参数都是self）'''
                args=args[1:]
                next_step(instance,fun.__name__,fun.__name__+"："+repr(e),*args,**kwargs)
        return decotor

    @entrace
    def find_element(self):
        #定位元素，返回一个元素
        locator=self.locator
        return driver.find_element(locator[0], locator[1])


    #返回一个元素
    def element(self):
        #返回一个元素
        return self.find_element()

    #清空元素
    def clear(self):
        #清空元素
        try:
            from selenium import webdriver
            self.find_element().clear()
        except Exception as e:
            next_step("self.clear","清空错误："+repr(e))

    #点击元素
    def click(self):
        #点击元素
        try:
            from selenium import webdriver
            element=self.find_element()
            driver.execute_script("arguments[0].scrollIntoView();",element)
            element.click()
        except Exception as e:
            next_step("self."+self.click.__name__,"点击错误："+repr(e))

    #通过js点击元素，暂时只支持几种定位器
    def js_click(self):
        '''
        #通过js点击元素，支持定位器：By.CSS_SELECTOR、By.ID、By.NAME
        '''
        if locator[0] == By.CSS_SELECTOR:
            js = '''document.querySelector("''' + locator[1] + '''").click()'''
        elif locator[0] == By.ID:
            js = '''document.getElementById("''' + locator[1] + '''").click()'''
        elif locator[0] == By.NAME:
            js = '''document.getElementByName("''' + locator[1] + '''").click()'''
        else:
            js=""
            print("js_click()函数不支持的选择器！")
        driver.execute_script(js)       

    #给元素传值
    def send_keys(self,value):
        '''
        给元素传值
        参数 value：需传入的值
        '''
        try:
            from selenium import webdriver
            self.find_element().send_keys(value)
        except Exception as e:
            next_step("self.send_keys","传值错误："+repr(e),value)

    '''
    #标准Select元素，选择方法
    '''
    def select(self,value,by="visible_text"):
        '''
        #标准Select元素，选择方法
        value:选项值，不同by选项需选择不同值
        参数 by:
        by选项：
            index:按index选择
            value:按option的value值选择
            visible_text:按可视文本选择
        '''
        try:
            from selenium.webdriver.support.ui import Select
            instance=Select(self.find_element())
            if by=="index":
                instance.select_by_index(value)
            elif by=="value":
                instance.select_by_value(value)
            elif by=="visible_text":
                instance.select_by_visible_text(value)
        except Exception as e:
           next_step("self.select",repr(e),value,by)     

    #获取元素属性值   
    def get_attribute(self,attribute):
        '''
        参数 attribute：属性值
        attribute选项：
            value：元素的值
            text：文本内容
            innerText：文本内容
            其它选项
        '''
        if attribute=="text":
            attribute="innerText"
        try:
            from selenium import webdriver
            self.find_element().get_attribute(attribute)
        except Exception as e:
           next_step("self.get_attribute","获取属性错误："+repr(e),attribute)   

    #获取元素文本内容
    def get_text(self):
        #获取元素文本内容
        try:
            from selenium import webdriver
            return self.find_element().text
        except Exception as e:
            next_step("self.get_text","获取文本错误："+repr(e)) 

    #高亮元素
    def highlight(self):
        #获取元素文本内容
        element = self.find_element()
        driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", element
                                   , "background:green;border:5px so lid red;") 
   
    #修改元素的属性
    def set_attribute(self,attribute,value):
        '''
        参数 attribute：属性值
        attribute选项：
            value：元素的值
            text：文本内容
            innerText：文本内容
            其它选项
        参数 value：修改后元素的属性值
        '''
        if attribute=="text":
            attribute="innerText"
        element = self.find_element()
        driver.execute_script("arguments[0]."+attribute+"='"+value+"'",element)
    
    #显式等待元素，默认10s,间隔0.5s,返回Ture或False
    def exist(self, timeout=10, poll_frequency=0.5):
        '''
        #显式等待元素，默认10s,间隔0.5s
        参数 timeout：超时时间
        参数 poll_frequency：查找元素时间间隔
        '''
        locator=self.locator
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        try:
            WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
            return True
        except:
            return False  

    #鼠标悬浮
    def focus(self):
        #鼠标悬浮到元素，元素为空悬浮于当前位置
        try:
            element=self.find_element()
            self.ActionChains(self.driver).move_to_element(element).perform()
        except Exception as e:
            next_step("focus","悬浮错误："+repr(e))

    #点击左键
    def left_click(self):
        #点击左键，如果元素为空，点击当前鼠标所在位置
        try:
            element=self.find_element()
            self.ActionChains(self.driver).click(element).perform()
        except Exception as e:
            next_step("left_click","左键点击错误："+repr(e))

    #双击左键
    def double_click(self):
        #双击左键，如果元素为空，点击当前鼠标所在位置
        try:
            element=self.find_element()
            self.ActionChains(self.driver).double_click(element).perform()
        except Exception as e:
            next_step("left_click","左键双击错误："+repr(e))
        

    #点击左键，不松开
    def click_and_hold(self):
        #点击左键，不松开，如果元素为空，点击当前鼠标所在位置
        try:
            element=self.find_element()
            self.ActionChains(self.driver).click_and_hold(element).perform()
        except Exception as e:
            next_step("left_click","左键点击保持错误："+repr(e))

    #点击右键
    def right_click(self):
        #点击右键，如果元素为空，点击当前鼠标所在位置
        try:
            element=self.find_element()
            self.ActionChains(self.driver).context_click(element).perform()
        except Exception as e:
            next_step("left_click","右键点击错误："+repr(e))


#判断弹框是否存在
def is_alert_present():
    from selenium.common.exceptions import NoSuchElementException
    try:
        driver.switch_to_alert()
    except NoAlertPresentException as e:
        return False
    return True    

#关闭弹框并获取弹框内容
def close_alert_and_get_its_text():
    from selenium.common.exceptions import NoAlertPresentException
    try:
        alert = driver.switch_to_alert()
        alert_text = alert.text
        if accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text
    finally:
        accept_next_alert = True





#辅助函数，find_element类中其他函数出错时下一步处理判断
def next_step(instance,name,error,*args,**kwargs):
    '''
    #辅助函数，find_element类中其他函数出错时下一步处理判断
    参数 name：错误函数的名称
    参数 error：错误函数的报错信息
    参数 *args：错误函数所需的参数变量集（有 传参数名）
    参数 **kwargs：错误函数所需的参数变量集（未传参数名）
    '''
    #print("Function_name:"+name)
    print(args)
    print(kwargs)
    temp_relay=relay
    if temp_relay==1:
        print("跳过操作，错误信息："+error)
    elif temp_relay==2: 
        temp_relay=pop_up_box(error)
        if int(temp_relay)==2:
            print("重新执行，错误信息："+error)
            #eval(name)(*args,**kwargs)
            #name.find_element(*args,**kwargs)
            getattr(instance,name)(*args,**kwargs)
        elif int(temp_relay)==1:
            print("跳过操作，错误信息："+error)
        elif temp_relay==3:
            print("停止执行，错误信息："+error)
            print("解释器主动退出，抛出异常信息！")
            quit()
        else:
            print("next_step()方法选项异常，请检查！")
    elif temp_relay==3:
        print("停止执行，错误信息："+error)
        print("解释器主动退出，抛出异常信息！")
        quit()
    else:
        temp_relay=1
        print("next_step()方法选项异常，自动默认为1，跳过操作！")

# 弹出一个窗口并返回输入的值
def pop_up_box(pop_text):
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
    #
    mycontent="       "+mycontent
    for i in range(0,10):
        if i==0:
            text="错误信息："
        if len(mycontent)!=0:
            text=text+"\n"+mycontent[0:70]
            mycontent=mycontent[50:len(mycontent)]
        else:
            print("判断")
            text=text+"\n       详细错误信息请见：日志目录"
            return text
            break