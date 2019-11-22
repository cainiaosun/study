# 本模块是借用selenium的方法及模块封装的一套自己的元素识别与操作的模块，功能包括：
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.common.keys import Keys
from base.web_ui.webelement_local import *
from base.web_ui.get_config import MyConfig
# from Function_sup import *
# import 鼠标键盘事件 as event

# 运行控制参数
relay = 2  # relay：错误处理选项：1.跳过；2.重新执行；3.停止。

# 浏览器启动参数
browser = "Chrome"  # 设置启动浏览器类型
excutable_path = None  # 设置driver文件路径
browser_binary = None  # 设置启动浏览器位置
global _driver
_driver=None

#print('fafather is:',dir(webelement_local))

class Browser:
    def __init__(self):
        pass
    
    def select_driver(self,driver):
        _driver = driver
        return driver

    def open(self):
        global _driver
        if browser in ("Firefox", "火狐", "火狐浏览器"):
            executable_path = MyConfig('driver','chromdriver').get_value()
            _driver = webdriver.Firefox(firefox_profile=None, firefox_binary=None,
                                       timeout=30, capabilities=None, proxy=None,
                                       executable_path=executable_path, options=None,
                                       log_path="geckodriver.log", firefox_options=None,
                                       service_args=None)
        elif browser in ("Chrome", "谷歌", "谷歌浏览器"):
            executable_path = MyConfig('driver','chromdriver').get_value()
            _driver = webdriver.Chrome(executable_path=executable_path, port=0,
                                      options=None, service_args=None,
                                      desired_capabilities=None, service_log_path=None,
                                      chrome_options=None)
        elif browser in ("IE", "Ie", "ie", "IE浏览器", "Ie浏览器", "ie浏览器"):
            _driver = webdriver.Ie(executable_path='IEDriverServer.exe', capabilities=None,
                                  port=DEFAULT_PORT, timeout=DEFAULT_TIMEOUT, host=DEFAULT_HOST,
                                  log_level=DEFAULT_LOG_LEVEL, log_file=DEFAULT_LOG_FILE, options=None,
                                  ie_options=None)
        return _driver

    def current_browser(self):
        '''
        获取当前的浏览器对象
        '''
        return _driver
    
    def switch_to_browser(self,browser):
        '''
        切换到指定的浏览器对象
        args:
            --browser:浏览器对象
        '''
        global _driver
        _driver = browser
        return _driver
    
    def goto(self,url):
        '''
        访问指定网址
        args:
            --url:需要访问的url地址
        '''
        _driver.get(url)

    def handles(self):
        '''
        获取当前所有的窗口句柄
        '''
        return _driver.window_handles
    
    def current_handle(self):
        '''
        获取当前窗口句柄
        '''
        return _driver.current_window_handle

    def switch_to_window(self,handle):
        '''
        浏览器窗口切换
        args:
            --handle:需要切换到的窗口的句柄
        '''
        _driver.switch_to_window(handle)

    def maximize(self):
        '''
        窗口最大化
        '''
        _driver.maximize_window()

    def minimize(self):
        '''
        窗口最小化
        '''
        _driver.minimize_window()

    def setsize(self,width,height):
        '''
        设置窗口大小
        args:
            --width:窗口长度
            --height:窗口高度
        '''
        _driver.set_window_size(width, height)

    def screenshot(self,path):
        '''
        截图并保存到指定目录
        args:
            --path:截图保存路径
        '''
        _driver.save_screenshot(path)

    def timeout(self,secs=60):
        '''
        隐式等待,设置浏览器元素加载默认超时时间
        args:
            --secs:超时时间，单位s(秒)，默认60s
        '''
        _driver.implicitly_wait(secs)

    def get_position(self):
        '''
        获取窗口位置
        '''
        return _driver.get_window_position()
    
    def set_position(self,x,y):
        '''
        设置浏览器窗口位置
        args:
            --x:窗口位置横坐标
            --y:窗口位置纵坐标
        '''
        _driver.set_window_position(x,y)

    def new_tab(self):
        '''
        打开新的tab页
        '''
        current_window=self.current_handle()
        _driver.execute_script("""window.open('','_blank')""")
        self.switch_to_window(current_window)

    
    

# 判断弹框是否存在
def is_alert_present():
    from selenium.common.exceptions import NoSuchElementException
    try:
        driver.switch_to_alert()
    except NoAlertPresentException as e:
        return False
    return True

# 关闭弹框并获取弹框内容
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

# 等待


def sleep(seconds):
    time.sleep(seconds)

# 定位操作操作的单个元素





if __name__ == '__main__':
    print(MyConfig('driver','chromdriver').get_value())
    Browser().open()
#    pass
    '''
    #help(Browser())
    dr1 = Browser().open()
    print(Browser().current_browser())
    #dr2 = Browser().open()
    #print(Browser().current_browser())
    #Browser().switch_to_browser(dr1)
    #print(Browser().current_browser())
    Browser().goto('https://www.baidu.com')
    Browser().get_position()
    Browser().set_position(30,30)
    print(Browser().handles())
    Browser().new_tab()
    print(Browser().handles())
    handles = Browser().handles()
    print(Browser().current_handle())
    Browser().switch_to_window(handles[1])
    Browser().switch_to_window(handles[0])
    Element(('id','kw')).find_element()
    element=_driver.find_element('id','kw')
    _driver.execute_script("arguments[0].value='时间'", element)
    '''
    '''
    Browser().goto()
    Browser().select()
    Browser().handles()
    Browser().save_screenshot()
    Browser().switch_to_frame()
    Browser().switch_to_browser()
    Browser().switch_to_window()
    Element().highlight()
    Element().element()
    Element().get_attribute()
    Elements().count()
    Elements().elements()
    Elements().
    #creat_driver()
    #get('http://www.baidu.com')
    #Element(('id','kw')).send_keys('123213213233')
    #save_screenshot('./test.png')
    #Switch_to.window('')
    #Switch_to.frame('')
'''
