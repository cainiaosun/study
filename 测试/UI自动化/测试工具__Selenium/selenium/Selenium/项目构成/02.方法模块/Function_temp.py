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

'''对于一些使用元素定位的方法，先进行元素定位判断，如果定位报错，那么就不执行该方法，
以避免因定位错误抛出一连串的错误,find_element/find_elements类中放心使用，其它地方
使用注意一下参数的设置'''
def check(func):
    def check_decorator(*args,**kwargs):
        try:
            '''类的公有方法的第一个参数是self，是类的实例，判断传过来的args[0](即self)
            参数是不是find_element或find_elements类中的方法，如果是，按照类里面元
            素的判断处理，如果不是，那么参数args[0]、args[1]组成的参数要是一个locator'''
            if isinstance(args[0],find_element):
                element=args[0].find_element()
            elif isinstance(args[0],find_elements):
                element=args[0].element()
            else:
                #这一个分支容易出错，什么时候遇到错误的时候再调整
                element=find_element(args[0]).find_element()
        except Exception as e:
            element=None
        #元素定位成功，执行内层方法
        if element!=None:
            func(*args,**kwargs)
    return check_decorator

#这个装饰器可用于本文档内所有的方法的异常循环执行处理，但是内部可能有些问题，以后遇见处理
def entrace(func):
    def decorator(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            #这个if是判断第一个参数是不是实例来的，但是感觉这个判断很差劲，以后水平提升一些后来改
            if len(str(type(args[0])).split("."))>1:
                #print("实例分支！")
                instance=args[0]
                args=args[1:]
                name=func.__name__
            else:
                #print("非实例分支！")
                instance=None
                args=args
                name=func.__qualname__
                #print(name)
            import traceback
            detail_error="traceback.format_exc:\n%s"%traceback.format_exc()       
            error=str(locals()['func']).split(" ")[1]+"："+repr(e)
            next_step(instance,name,error,detail_error,*args,**kwargs)
    return decorator


#辅助函数，我们这里只应用于entrace()函数中，共同处理异常后续操作
def next_step(instance,name,error,detail_error,*args,**kwargs):
    '''
    #辅助函数，find_element类中其他函数出错时下一步处理判断
    参数 name：错误函数的名称
    参数 error：错误函数的报错信息
    参数 *args：错误函数所需的参数变量集（有 传参数名）
    参数 **kwargs：错误函数所需的参数变量集（未传参数名）
    '''
    print("进入")
    temp_relay=relay
    if temp_relay==1:
        print("跳过操作，错误信息："+error)
    elif temp_relay==2: 
        temp_relay=pop_up_box(error)
        if int(temp_relay)==2:
            print("重新执行，错误信息："+error)
            #eval(name)(*args,**kwargs)
            #name.find_element(*args,**kwargs)
            if instance:
                getattr(instance,name)(*args,**kwargs)
            else:
                eval(name)(*args,**kwargs)
        elif int(temp_relay)==1:
            print("跳过操作，错误信息："+error)
        else:
            print("停止执行，错误信息："+error)
            raise Exception(detail_error)
    else:
        print("停止执行，错误信息："+error)
        raise Exception(detail_error)


# 弹出一个窗口并根据点击按钮返回一个值，我们只应用于next_step()函数中，共同处理异常后续操作
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
            #print("出错时，弹出框输入判断！")
            text=text+"\n       详细错误信息请见：日志目录"
            return text
            break

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

#定位操作操作的单个元素
class find_element():
    '''
    find_element()定位元素，返回一个元素
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
    def __init__(self,locator="",driver=driver):
        """
        #初始化函数
        参数 locator：选择器，形式(By.ID)
        参数 relay：错误处理选项：1.跳过；2.重新执行；3.停止。
        """
        self.locator=locator
        self.relay=relay
        from selenium.webdriver.common.action_chains import ActionChains
        self.ActionChains=ActionChains
        self.driver=driver


    #定位元素，返回一个元素
    @entrace
    def find_element(self):
        #定位元素，返回一个元素
        locator=self.locator
        return driver.find_element(locator[0], locator[1])

    #返回一个元素
    @check
    @entrace
    def element(self):
        #返回一个元素
        return self.find_element()

    #清空元素
    @check
    @entrace
    def clear(self):
        #清空元素
        self.find_element().clear()

    #移动到元素可见，可以理解为操作滚动条
    @check
    @entrace
    def scroll_into_view(self):
        #点击元素
        element=self.find_element()
        driver.execute_script("arguments[0].scrollIntoView();",element)

    #左键单击元素
    @check
    @entrace
    def click(self):
        #左键单击元素
        element=self.find_element()
        element.click()

    #左键单击元素：移动元素到可见，并左键单击元素左上角对应x,y个单位，默认点击元素中间
    @check
    @entrace
    def click_on(self,xoffset=None,yoffset=None):
        '''
        xoffset:相对于元素左上角的x个单位
        xoffset:相对于元素左上角的y个单位
        '''
        element=self.find_element()
        print("element:"+str(element))
        if element:  
            driver.execute_script("arguments[0].scrollIntoView();",element)
            self.ActionChains(driver).move_to_element_with_offset(element,xoffset,yoffset)\
            .click().perform()


    #通过js点击元素，暂时只支持几种定位器
    @entrace
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
    @check
    @entrace
    def send_keys(self,value):
        '''
        给元素传值
        参数 value：需传入的值
        '''
        self.find_element().send_keys(value)


    '''
    #标准Select元素，选择方法
    '''
    @check
    @entrace
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
        from selenium.webdriver.support.ui import Select
        instance=Select(self.find_element())
        if by=="index":
            instance.select_by_index(value)
        elif by=="value":
            instance.select_by_value(value)
        elif by=="visible_text":
            instance.select_by_visible_text(value)
 

    #获取元素属性值 
    @check
    @entrace  
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
        self.find_element().get_attribute(attribute)


    #高亮元素
    @check
    @entrace
    def highlight(self):
        #获取元素文本内容
        element = self.find_element()
        driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", element
                                   , "background:green;border:5px so lid red;") 
   
    #修改元素的属性
    @check
    @entrace
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
    @entrace
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
    @check
    @entrace
    def focus(self):
        #鼠标悬浮到元素，元素为空悬浮于当前位置
        element=self.find_element()
        self.ActionChains(self.driver).move_to_element(element).perform()

    #点击左键
    @check
    @entrace
    def left_click(self):
        #点击左键，如果元素为空，点击当前鼠标所在位置
        element=self.find_element()
        self.ActionChains(self.driver).click(element).perform()

    #双击左键
    @check
    @entrace
    def double_click(self):
        #双击左键，如果元素为空，点击当前鼠标所在位置
        element=self.find_element()
        self.ActionChains(self.driver).double_click(element).perform()

    #点击左键，不松开
    @check
    @entrace
    def click_and_hold(self):
        #点击左键，不松开，如果元素为空，点击当前鼠标所在位置
        element=self.find_element()
        self.ActionChains(self.driver).click_and_hold(element).perform()

    #点击右键
    @check
    @entrace
    def right_click(self):
        #点击右键，如果元素为空，点击当前鼠标所在位置
        element=self.find_element()
        self.ActionChains(self.driver).context_click(element).perform()

    #获取元素文本内容
    @check
    @property
    @entrace
    def text(self):
        #获取元素文本内容
        return self.find_element().text

    #获取元素的大小值
    @check
    @property
    @entrace
    def size(self):
        element=self.find_element()
        return element.size

    #获取元素的坐标
    @check
    @property
    @entrace
    def location(self):
        element=self.find_element()
        return element.location



#切换iframe页面
class switch_to(object):
    @check
    @entrace
    @staticmethod
    def frame(locator):
        frame=find_element(locator).find_element()
        if frame!=None:
            driver.switch_to.frame(frame)

    @entrace
    @staticmethod
    def default_content():
        driver.switch_to.default_content()



#定位操作操作的单个元素
class find_elements():
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
    def __init__(self,locator="",driver=driver,index=None):
        """
        #初始化函数
        参数 locator：选择器，形式(By.ID)
        参数 relay：错误处理选项：1.跳过；2.重新执行；3.停止。
        """
        self.locator=locator
        self.relay=relay
        from selenium.webdriver.common.action_chains import ActionChains
        self.ActionChains=ActionChains
        self.driver=driver
        self.index=index


    #定位元素，返回一个元素
    @entrace
    def find_elements(self):
        #定位元素，返回一个元素
        locator=self.locator
        return driver.find_elements(locator[0], locator[1])

    #返回一个元素
    @check
    @entrace
    def elements(self):
        #返回一个元素
        return self.find_elements()

    #返回一个元素
    @check
    @entrace
    def element(self):
        #返回一个元素
        return self.find_elements()[index]