#本模块是借用selenium的方法及模块封装的一套自己的元素识别与操作的模块，功能包括：
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
sys.path.append(".//")
# from Function_sup import *
# import 鼠标键盘事件 as event

#运行控制参数
relay=2 #relay：错误处理选项：1.跳过；2.重新执行；3.停止。

#浏览器启动参数
browser="Firefox"   #设置启动浏览器类型
excutable_path=None   #设置driver文件路径
browser_binary=None   #设置启动浏览器位置
driver=""
# driver=webdriver.Firefox()   #命名浏览器对象
#通过上面设置，对driver重新赋值一个WebDriver对象


def creat_driver():
    if browser in ("Firefox","火狐","火狐浏览器"):      
        executable_path="F:/GIT文件/Study/测试/UI自动化/Selenium/driver/firefox/geckodriver-v0.24.0-win64/geckodriver.exe"
        driver=webdriver.Firefox(firefox_profile=None, firefox_binary=None,
                 timeout=30, capabilities=None, proxy=None,
                 executable_path=executable_path, options=None,
                 log_path="geckodriver.log", firefox_options=None,
                 service_args=None)
    elif browser in ("Chrome","谷歌","谷歌浏览器"):
        driver=webdriver.Chrome(executable_path="chromedriver", port=0,
                 options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None,
                 chrome_options=None)
    elif browser in ("IE","Ie","ie","IE浏览器","Ie浏览器","ie浏览器"):
        driver=webdriver.Ie(executable_path='IEDriverServer.exe', capabilities=None,
                 port=DEFAULT_PORT, timeout=DEFAULT_TIMEOUT, host=DEFAULT_HOST,
                 log_level=DEFAULT_LOG_LEVEL, log_file=DEFAULT_LOG_FILE, options=None,
                 ie_options=None)
    return driver

def get(url):
    return driver.get(url)

#获取所有窗口句柄
def window_handles():
    return driver.window_handles()

#获取当前窗口句柄
def current_handle():
    return driver.current_handle()

#窗口最大化
def maximize():
    driver.maximize_window()

#窗口最小化
def minimize():
    driver.minimize_window()

#窗口最小化
def setsize(width,height):
    driver.set_window_size(width,height)

#判断弹框是否存在
def is_alert_present():
    from selenium.common.exceptions import NoSuchElementException
    try:
        driver.switch_to_alert()
    except NoAlertPresentException as e:
        return False
    return True    

def save_screenshot(filepath):
    driver.save_screenshot(filepath)

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

#隐式等待
def implicitly_wait(timeout=60):
    driver.implicitly_wait(timeout)

#等待
def sleep(seconds):
    time.sleep(seconds)

#定位操作操作的单个元素
class Element():
    '''
    find_element()定位元素,返回一个元素
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
        参数：
        -locator：选择器，如(By.ID,id),如果输入为字符串，默认转换为(By.XPATH,str)形式
        -relay：错误处理选项：1.跳过；2.重新执行；3.停止
        """
        if isinstance(locator,str):
            #locator为字串时，转为XPATH形式选择器
            self.locator=(By.XPATH,locator)
        elif isinstance(locator,tuple):
            #locator为元组时，输入必须符合选择器形式，直接使用
            self.locator=locator
        else:print("locator参数不符合要求！")
        self.relay=relay
        #下面两个步骤有待商定
        from selenium.webdriver.common.action_chains import ActionChains
        self.ActionChains=ActionChains
        self.driver=driver

    #定位元素，返回一个元素,给装饰器调用判断的元素是否存在使用
    def find_element(self):
        #定位元素，返回一个元素,给装饰器调用判断的元素是否存在使用
        locator=self.locator
        return driver.find_element(locator[0], locator[1])

    #定位元素，返回一个元素
    # @outerentrace(False)
    def element(self):
        #定位元素，返回一个元素
        locator=self.locator
        return driver.find_element(locator[0], locator[1])

    #清空元素
    # @outerentrace()
    def clear(self):
        #清空元素
        self.element().clear()

    #移动到元素可见，可以理解为操作滚动条
    # @outerentrace()
    def scroll_into_view(self):
        #移动到元素可见，可以理解为操作滚动条
        element=self.element()
        driver.execute_script("arguments[0].scrollIntoView();",element)

    #左键点击元素
    # @outerentrace()
    def click(self):
        #左键点击元素
        self.element().click()

    #左键单击元素：移动元素到可见，并左键单击元素左上角对应x,y个单位，默认点击元素中间
    # @outerentrace()
    def click_on(self,xoffset=None,yoffset=None):
        '''
        左键单击元素：移动元素到可见，并左键单击元素左上角对应x,y个单位，默认点击元素中间
        参数：
        xoffset:相对于元素左上角的x个单位
        xoffset:相对于元素左上角的y个单位
        '''
        element=self.element()
        print("element:"+str(element))
        if element:  
            driver.execute_script("arguments[0].scrollIntoView();",element)
            self.ActionChains(driver).move_to_element_with_offset(element,xoffset,yoffset)\
            .click().perform()


    #通过js点击元素，暂时只支持几种定位器
    # @outerentrace(False)
    def js_click(self):
        '''
        通过js点击元素，支持定位器：By.CSS_SELECTOR、By.ID、By.NAME
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
    # @outerentrace(False)
    def send_keys(self,value):
        '''
        给元素传值
        参数:
        -value：需传入的值
        '''
        self.element().send_keys(value)


    #标准Select元素，选择方法    
    # @outerentrace()
    def select(self,value,by="visible_text"):
        '''
        标准Select元素，选择方法
        参数:
        -value:根据by输入的选择定位的值，不同by选项需输入不同的值
        -by:选择的方式
            by选项：
                index:按index选择
                value:按option的value值选择
                visible_text:按可视文本选择
        '''
        from selenium.webdriver.support.ui import Select
        instance=Select(self.element())
        if by=="index":
            instance.select_by_index(value)
        elif by=="value":
            instance.select_by_value(value)
        elif by=="visible_text":
            instance.select_by_visible_text(value)
 

    #获取元素属性值     
    # @outerentrace()  
    def get_attribute(self,attribute):
        '''
        获取元素属性值
        参数：
        -attribute：属性值
            attribute选项：
                value：元素的值
                text：文本内容
                innerText：文本内容
                其它选项
        '''
        if attribute=="text":
            attribute="innerText"
        self.element().get_attribute(attribute)


    #高亮元素    
    # @outerentrace(False)
    def highlight(self):
        #高亮元素
        element = self.element()
        driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", 
            element, "background:green;border:5px so lid red;") 
   
    #修改元素的属性   
    # @outerentrace()
    def set_attribute(self,attribute,value):
        '''
        修改元素的属性
        参数：
        -attribute：属性值
            attribute选项：
                value：元素的值
                text：文本内容
                innerText：文本内容
                其它选项
        -value：修改后元素的属性值
        '''
        if attribute=="text":
            attribute="innerText"
        element = self.element()
        driver.execute_script("arguments[0]."+attribute+"='"+value+"'",element)
    
    #显式等待元素，默认10s,间隔0.5s,返回Ture或False
    def exist(self, timeout=10, poll_frequency=0.5):
        '''
        显式等待元素，默认10s,间隔0.5s
        参数：
        -timeout：超时时间
        -poll_frequency：查找元素时间间隔
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
    # @outerentrace()
    def focus(self):
        #鼠标悬浮到元素，元素为空悬浮于当前位置
        element=self.element()
        self.ActionChains(self.driver).move_to_element(element).perform()

    #点击左键   
    # @outerentrace()
    def left_click(self):
        #点击左键，如果元素为空，点击当前鼠标所在位置
        element=self.element()
        self.ActionChains(self.driver).click(element).perform()

    #双击左键   
    # @outerentrace()
    def double_click(self):
        #双击左键，如果元素为空，点击当前鼠标所在位置
        element=self.element()
        self.ActionChains(self.driver).double_click(element).perform()

    #点击左键，不松开   
    # @outerentrace()
    def click_and_hold(self):
        #点击左键，不松开，如果元素为空，点击当前鼠标所在位置
        element=self.element()
        self.ActionChains(self.driver).click_and_hold(element).perform()

    #点击右键    
    # @outerentrace()
    def right_click(self):
        #点击右键，如果元素为空，点击当前鼠标所在位置
        element=self.element()
        self.ActionChains(self.driver).context_click(element).perform()

    #获取元素文本内容  
    @property
    # @outerentrace()
    def text(self):
        #获取元素文本内容
        return self.element().text

    #获取元素的大小值    
    @property
    # @outerentrace()
    def size(self):
        #获取元素的大小值
        element=self.element()
        return element.size

    #获取元素的坐标    
    @property
    # @outerentrace()
    def location(self):
        #获取元素的坐标
        element=self.element()
        return element.location


#切换iframe页面或windows窗口
class Switch_to(object):
    #初始化函数
    def __init__(self):
        pass
 
    @staticmethod
    #@check_error
    def frame(locator):
        frame=Element(locator).element()
        if frame!=None:
            driver.switch_to.frame(frame)

    @staticmethod
    #@check_error
    def default_content():
        driver.switch_to.default_content()

    @staticmethod
    #@check_error
    def window(window_handle):
        driver.switch_to.window(window_handle)



if __name__=='__main__':
    creat_driver()