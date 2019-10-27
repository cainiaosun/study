from base.web_ui.webdriver import *

#Browser().select_element()
#Browser().select_case()
def test():
    Browser().open()
    Browser().goto('http://www.baidu.com')
    Element('id','kw').input('123')
    Element('百度一下按钮').click()