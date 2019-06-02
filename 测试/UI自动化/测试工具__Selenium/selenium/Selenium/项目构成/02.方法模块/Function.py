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

'''装饰器函数，对于find_element类中一些有用到element的方法，我们先对element做判断处理，如果通过再对被调用的
方法进行处理，减少因element抛出的可预知的坠余异常判断处理信息'''
def check(fun):
    def check_decorator(*args,**kwargs):
        instance=args[0]
        #if isinstance(instance,find_element) or isinstance(instance,find_elements):
        try:
                element=instance.find_element()
        except Exception as e:
            element=None
            import traceback
            detail_error="traceback.format_exc:\n%s"%traceback.format_exc()
            '''我们在这里抛出一个异常是因为检查的时候把调用find_element()方法，选择终止操作时抛出异常掩
            盖掉，导致效果类似于跳过该步骤'''
            raise Exception("check_exception:异常处理手工抛错，请检查异常处理前抛出的错误！")
        if element!=None:
            fun(*args,**kwargs)
    return check_decorator

'''装饰器函数,异常时对下一步操作的处理，暂时应用于find_element()类和find_elements()类中
关于类里面调用类外面的函数有很多疑惑，比如装饰器@entrace,如果entrace放在find_element类所在后面，那么
会报错没有定义entrace，放类内部或find_element前面就正常了。但是呢，如果我们在类里面世界调用外部函数是
是可以调用成功，比如我们调用next_step函数'''
def entrace(fun):
    '''fun:解取被装饰函数的函数实例（注：这个fun存储的实例在其他地方使用，但是被调用时是直接调用
    不会再调用一次装饰函数）'''
    def decorator(*args,**kwargs):
        #*args:接取被装饰函数传参未带参数名的参数，如：function(1,2,c=5)中的1和2参数
        #**kwargs:接取被装饰函数传参带有参数名的参数，如：function(1,2,c=5)中的5参数
        try:
            return fun(*args,**kwargs)
        except Exception as e:
            #print("处理异常")
            #类的实例参数（注：类的实例参数可以在其他地方调用）
            instance=args[0]
            '''去除self(类的实例)后调用方法的剩余不参数名的参数（注：被装饰函数都是类的公有函数
            所以第一个参数都是self）'''
            args=args[1:]
            #error
            error=str(locals()['fun']).split(" ")[1]+"："+repr(e)
            import traceback
            detail_error="traceback.format_exc:\n%s"%traceback.format_exc()
            next_step(instance,fun.__name__,error,detail_error,*args,**kwargs)
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
        else:
            print("停止执行，错误信息："+error)
            raise Exception("next_step_exception:异常处理手工抛错，请检查异常处理前抛出的错误！")
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
    @staticmethod
    def frame(locator):
        frame=find_element(locator).find_element()
        if frame!=None:
            driver.switch_to.frame(frame)

    @staticmethod
    def default_content():
        driver.switch_to.default_content()