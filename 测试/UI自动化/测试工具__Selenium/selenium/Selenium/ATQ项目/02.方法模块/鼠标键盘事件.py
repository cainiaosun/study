#本模块方法套用ActionChains 类的方法，稍微看一下，没什么卵用，并没有比ActionChains类简单，
#但是还是自己封装一下，算是给给自己以后做个参考吧

#鼠标、键盘事件
class event():
    def __init__(self,driver,element=None):
        from selenium.webdriver.common.action_chains import ActionChains
        self.ActionChains=ActionChains
        self.element=element
        self.driver=driver


    #测试成功
    #单击左键
    def click(self,element=None):
        if self.element!=None:
            element=self.element
        self.ActionChains(self.driver).click(element).perform()

    #测试成功
    #双击左键
    def double_click(self,element=None):
        if self.element!=None:
            element=self.element
        self.ActionChains(self.driver).double_click(element).perform()

    #本方法功能测试成功，但是后续操作弹出框发送快捷键在Firefox上无效，且连续点击右键，弹出框刷险也没有跟随
    #坐标，故对右键操作对Firefox支持不好，如有需要需进一步修改。
    #单击右键
    def context_click(self,element=""):
        if self.element!=None:
            element=self.element
        self.ActionChains(self.driver).context_click(element).perform()

    #测试成功
    #单击左键不松开
    def click_and_hold(self,element=None):
        if self.element!=None:
            element=self.element
        self.ActionChains(self.driver).click_and_hold(element).perform()

    #测试成功
    #移动鼠标到元素,目标元素若为空会报错 
    def move_to_element(self,element=None):
        if self.element!=None:
            element=self.element
        self.ActionChains(self.driver).move_to_element(element).perform()

    #检测成功，注：若移动到屏幕外会报错
    #相对于当前坐标移动一定的坐标
    def move_by_offset(self,xoffset,yoffset):
        self.ActionChains(self.driver).move_by_offset(xoffset,yoffset).perform()

    #测试成功，注：若移动到屏幕外会报错
    #移动鼠标到元素左上角相对的某一坐标
    def move_to_element_with_offset(self,element,xoffset,yoffset):
        if self.element!=None:
            element=self.element
        self.ActionChains(self.driver).move_to_element_with_offset(element,xoffset,yoffset).perform()

    #测试成功
    #在元素上松开左键，元素为空时默认当前焦点
    def release(self,element=None):
        if self.element!=None:
            element=self.element
        self.ActionChains(self.driver).release(element).perform()

    #拖拽一个元素到另一个元素
    def drag_and_drop(self,souce,target):
        print("拖拽")
        if self.element!=None:
            souce=self.element
        #driver.execute_script("arguments[0].scrollIntoView();",souce)
        self.ActionChains(self.driver).drag_and_drop(souce,target).perform()

    #拖拽一个元素到一个指定坐标
    def drag_and_drop_by_offset(self,souce,xoffset,yoffset):
        if self.element!=None:
            souce=self.element
        self.ActionChains(self.driver).drag_and_drop_by_offset(souce,xoffset,yoffset).perform()

    #测试成功
    #在当前焦点，发送值
    def send_keys(self,*keys_to_send):
        self.ActionChains(self.driver).send_keys(*keys_to_send).perform()

    #未测试
    #对一个元素发送值
    def send_keys_to_element(self,element,*keys_to_send):
        if self.element!=None:
            element=self.element
        self.ActionChains(self.driver).send_keys_to_element(element,*keys_to_send).perform() 

    #测试成功
    #按下指定按键不松开
    def key_down(self,value,element=None):
        if self.element!=None:
            element=self.element
        self.ActionChains(self.driver).key_down(value,element).perform()

    #测试成功
    #松开指定按键
    def key_up(self,value,element=None):
        if self.element!=None:
            element=self.element
        self.ActionChains(self.driver).key_up(value,element).perform()