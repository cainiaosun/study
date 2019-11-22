#from base.web_ui import webdriver_local
#from base.web_ui.webdriver_local import Browser
from base.web_ui.getElement import getLocator
from base.web_ui.relay_entrace import relay_entrace
from selenium.webdriver.common.action_chains import ActionChains




class Element():
    '''
    find_element()定位元素,返回一个元素
    element()返回一个元素
    clear()清空元素
    click()点击元素
    click_by_js()通过js语句点击元素
    input()向元素传值
    select()标准select选择框选择方法
    get_attribute()获取元素属性，包括text
    text()获取文本
    highlight()高亮元素
    set_attribute()设置元素属性值，包括text
    exist()元素显式等待
    focus()悬浮鼠标到元素
    left_click()单击左键
    double_click()双击左键
    click_and_hold()点击左键不放开
    right_click()单击右键
    '''
    # 初始化函数
    @relay_entrace
    def __init__(self,locator="",pattern=None,timeout=None):
        """
        参数：
        -locator：选择器，如(By.ID,id),如果输入为字符串，默认转换为(By.XPATH,str)形式
        -relay：错误处理选项：1.跳过；2.重新执行；3.停止
        """
        #判断是否能够获得浏览器对象
        if webdriver_local._driver==None:
            print('未获取到启动的浏览器！')
        else:
            self._driver = webdriver_local._driver

        #判断输入参数形式，重新组装locator为一个元组
        if isinstance(locator, str):
            if pattern:
                self.locator = (locator,pattern)
            else:
                self.locator = getLocator().get()[locator]
            print('locator is :',self.locator)
        elif isinstance(locator, tuple):
            self.locator = locator
        else:
            raise Exception("定位器参数错误！")

        #判断选择器形式是否符合要求
        support_locator = ('id','name','xpath','css_selector')
        if self.locator[0] not in support_locator:
            raise Exception("不支持的定位器：%s，支持列表：%s" %(str(self.locator[0]),str(support_locator)))
        
        if timeout!=None:
            if self.exist(timeout):
                raise Exception("未找到元素")

        # 下面两个步骤有待商定
        self.ActionChains = ActionChains
        print(self.locator)
        self.check_init = True



    
    # 定位元素，返回一个元素,给装饰器调用判断的元素是否存在使用
    @relay_entrace
    def _find_element(self):
        # 定位元素，返回一个元素,给装饰器调用判断的元素是否存在使用
        locator = self.locator
        return webdriver_local._driver.find_element(locator[0], locator[1])

    # 定位元素，返回一个元素
    # @outerentrace(False)
    def element(self):
        return self._find_element()

    # 清空元素
    # @outerentrace()
    def clear(self):
        # 清空元素
        self.element().clear()

    # 移动到元素可见，可以理解为操作滚动条
    # @outerentrace()
    def scroll_into_view(self):
        # 移动到元素可见，可以理解为操作滚动条
        element = self.element()
        webdriver_local._driver.execute_script("arguments[0].scrollIntoView();", element)

    # 左键点击元素
    # @outerentrace()
    def click(self):
        # 左键点击元素
        self.element().click()

    # 左键单击元素：移动元素到可见，并左键单击元素左上角对应x,y个单位，默认点击元素中间
    # @outerentrace()
    def click_by_offset(self, xoffset=None, yoffset=None):
        '''
        左键单击元素：移动元素到可见，并左键单击元素左上角对应x,y个单位，默认点击元素中间
        参数：
        xoffset:相对于元素左上角的x个单位
        xoffset:相对于元素左上角的y个单位
        '''
        element = self.element()
        print("element:"+str(element))
        if element:
            webdriver_local._driver.execute_script("arguments[0].scrollIntoView();", element)
            self.ActionChains(webdriver_local._driver).move_to_element_with_offset(element, xoffset, yoffset)\
                .click().perform()

    # 通过js点击元素，暂时只支持几种定位器
    # @outerentrace(False)

    def click_by_js(self):
        '''
        通过js点击元素，支持定位器：By.CSS_SELECTOR、By.ID、By.NAME
        '''
        if locator[0] == By.CSS_SELECTOR:
            js = '''document.querySelector("''' + locator[1] + '''").click()'''
        elif locator[0] == By.ID:
            js = '''document.getElementById("''' + \
                locator[1] + '''").click()'''
        elif locator[0] == By.NAME:
            js = '''document.getElementByName("''' + \
                locator[1] + '''").click()'''
        else:
            js = ""
            print("js_click()函数不支持的选择器！")
        webdriver_local._driver.execute_script(js)

    # 给元素传值
    # @outerentrace(False)
    def input(self, value):
        '''
        给元素传值
        参数:
        -value：需传入的值
        '''
        self.element().send_keys(value)
    
    def input_by_js(self):
        pass

    # 标准Select元素，选择方法
    # @outerentrace()
    def select(self, value, by="visible_text"):
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
        from selenium.web_driver.support.ui import Select
        instance = Select(self.element())
        if by == "index":
            instance.select_by_index(value)
        elif by == "value":
            instance.select_by_value(value)
        elif by == "visible_text":
            instance.select_by_visible_text(value)

    # 获取元素属性值
    # @outerentrace()

    def get_attribute(self, attribute):
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
        if attribute == "text":
            attribute = "innerText"
        self.element().get_attribute(attribute)

    # 高亮元素
    # @outerentrace(False)
    @relay_entrace
    def highlight(self):
        # 高亮元素
        element = self.element()
        if element:
            webdriver_local._driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
                              element, "background:green;border:5px so lid red;")

    # 修改元素的属性
    # @outerentrace()
    def set_attribute(self, attribute, value):
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
        if attribute == "text":
            attribute = "innerText"
        element = self.element()
        _driver.execute_script(
            "arguments[0]."+attribute+"='"+value+"'", element)

    # 显式等待元素，默认10s,间隔0.5s,返回Ture或False
    def exist(self, timeout=10, poll_frequency=0.5):
        '''
        显式等待元素，默认10s,间隔0.5s
        参数：
        -timeout：超时时间
        -poll_frequency：查找元素时间间隔
        '''
        locator = self.locator
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        try:
            Web_driverWait(_driver, timeout, poll_frequency).until(
                EC.presence_of_element_located(locator))
            print("你真是蠢")
            return True
        except:
            print("你真对的")
            return False

    # 鼠标悬浮
    # @outerentrace()
    def focus(self):
        # 鼠标悬浮到元素，元素为空悬浮于当前位置
        element = self.element()
        if element:
            self.ActionChains(self._driver).move_to_element(element).perform()

    # 点击左键
    # @outerentrace()
    def left_click(self):
        # 点击左键，如果元素为空，点击当前鼠标所在位置
        element = self.element()
        self.ActionChains(self._driver).click(element).perform()

    # 双击左键
    # @outerentrace()
    def double_click(self):
        # 双击左键，如果元素为空，点击当前鼠标所在位置
        element = self.element()
        self.ActionChains(self._driver).double_click(element).perform()

    # 点击左键，不松开
    # @outerentrace()
    def click_and_hold(self):
        # 点击左键，不松开，如果元素为空，点击当前鼠标所在位置
        element = self.element()
        self.ActionChains(self._driver).click_and_hold(element).perform()

    # 点击右键
    # @outerentrace()
    def right_click(self):
        # 点击右键，如果元素为空，点击当前鼠标所在位置
        element = self.element()
        self.ActionChains(self._driver).context_click(element).perform()

    # 获取元素文本内容
    @property
    # @outerentrace()
    def text(self):
        # 获取元素文本内容
        return self.element().text

    # 获取元素的大小值
    @property
    # @outerentrace()
    def size(self):
        # 获取元素的大小值
        element = self.element()
        return element.size

    # 获取元素的坐标
    @property
    # @outerentrace()
    def location(self):
        # 获取元素的坐标
        element = self.element()
        return element.location


# 切换iframe页面或windows窗口
class Switch_to(object):
    # 初始化函数
    def __init__(self):
        pass

    @staticmethod
    # @check_error
    def frame(locator):
        frame = Element(locator).element()
        if frame != None:
            _driver.switch_to.frame(frame)

    @staticmethod
    # @check_error
    def default_content():
        _driver.switch_to.default_content()

    @staticmethod
    # @check_error
    def window(window_handle):
        _driver.switch_to.window(window_handle)


if __name__=="__main__":
    webdriver_local.Browser().open()
    print('this is :',webdriver_local._driver)
    webdriver_local.Browser().goto('http://www.baidu.com')
    Element(('id','kw')).highlight()