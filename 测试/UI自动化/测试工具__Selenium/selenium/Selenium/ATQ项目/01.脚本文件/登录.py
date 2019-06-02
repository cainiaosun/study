import sys,time,unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
sys.path.append(".//")
sys.path.append(sys.path[0].split("ATQ项目")[0] + 'ATQ项目\\02.方法模块')
import Function_temp  as F

class ATQtest(unittest.TestCase):
    #driver全局变量
    option =webdriver.FirefoxOptions()
    option.set_headless()
    dr1 = webdriver.Firefox(firefox_options=option)#设置对象
    dr = webdriver.Firefox()#设置对象
    F.driver=dr
    def setUp(self,driver = dr):
        self.driver =driver#设置对象
        self.base_url = "http://11.8.127.248:8080/atq/frame.jsp"#网址
        self.username='sunhongbin'#登录用户名

    def test_01_login(self):
        #data
        print("登录ATQ！")
        username = self.username
        #page_element
        用户名输入框=(By.NAME,'loginId')
        密码输入框=(By.NAME,'password')
        登录按钮=(By.LINK_TEXT,'登录')
        #Script
        driver = self.driver
        self.driver.get(self.base_url)
        F.find_element(用户名输入框).clear()
        F.find_element(用户名输入框).send_keys(username)
        F.find_element(密码输入框).send_keys('123456')
        F.find_element(登录按钮).click()
        #等待
        time.sleep(3)

    def test_02_case_import(self):
        #data
        print("进入案例管理页面！")
        driver = self.driver
        #case_path=self.case_path
        #page
        案例管理菜单=(By.XPATH,"//span[contains(text(),'案例管理')]")
        需求管理菜单=(By.XPATH,"//span[contains(text(),'需求管理')]")
        xf=(By.XPATH,"/html/body/div[3]/div/div/div[2]/div[2]/div/iframe")
        加载提示=(By.XPATH,"//div[contains(text(),'Loading')]")
        导入案例按钮=(By.XPATH,"//span[text()='导入案例']")
        #Script
        print("导入案例！")
        F.find_element(案例管理菜单).click()
        time.sleep(2)
        #切换iframe页面
        #driver.switch_to.frame(F.find_element(xf).find_element())
        F.switch_to.frame(xf)
        print("切换成功？")
        time.sleep(5)
        if F.find_element(需求管理菜单):
            F.find_element(需求管理菜单).highlight()
            print(F.find_element(需求管理菜单))
            print("失败")
        else:
            print("成功")
        print("等待【案例管理_案例列表】页面加载...")
        print(F.find_elements(加载提示))
        for i in range(0,30):
            refresh=F.find_elements(加载提示).find_elements()
            print()
            if len(refresh)<2:
                print("【案例管理_案例列表】页面加载完成！")
                F.find_element(导入案例按钮).click()
                break
            else:
                print(i)
                time.sleep(3)             
        time.sleep(2)
        #上传按钮
        upload=driver.find_element_by_id("upload")
        upload.send_keys(case_path)
        value=upload.get_attribute('value')
        if value!="":
            print("文件上传成功！")
        driver.find_element_by_xpath("//span[text()='确定']").click()
        time.sleep(2)
        #判断页面的元素检查是否正在导入，默认先等30s
        if len(driver.find_elements_by_xpath("//div[contains(text(),'导入中，请稍候')]"))>0:
            print("导入中，请耐心等候...")
            time.sleep(30)
        #30s后通过判断导入结束的弹出窗口判断是否导入完毕，如果没有找到窗口则等待继续寻找窗口，直至寻找成功
        #回到主frame页
        driver.switch_to.default_content()
        for i in range(0,100):
            try:
                text=driver.find_element_by_xpath("/html/body/div[10]/div[2]").text
                print("案例导入完毕！")
                break
            except:
                time.sleep(0.01)
        time.sleep(5)
        #通过判断Loading元素，目录树页面是否加载成功，如果未加载成功则等待2s，反复循环
        self.driver.switch_to.frame(xf)
        print("等待【案例管理_案例目录】页面加载...")
        for i in range(0,100):
            refresh= driver.find_elements_by_xpath("//div[contains(text(),'Loading')]")
            if len(refresh)>0:
                time.sleep(2)
            else:
                print("【案例管理_案例目录】页面加载完成！")
                break
        #创建excel对象并取excel中的数据去判断目录树对应的目录是否已经存在，以此判断案例是否导入成功
        ex=openpyxl.load_workbook(case_path)
        sh=ex[ex.sheetnames[0]]
        print("案例目录检查...")
        if self.isElementExist("by.xpath","//span[text()='"+sh['C2'].value+"']/../../../following-sibling::tr[1]//span[text()='"+sh['D2'].value+"']"):
            print("案例目录检查完毕，案例目录存在，案例导入成功！")
        else:print("案例目录检查完毕，未发现案例目录，案例导入失败！")
        #回到主frame页
        driver.switch_to.default_content()
        time.sleep(5)



    def tearDown(self):
        pass
        #self.driver.quit()#这里有多个test需要用到driver，所以tearDown中，不要关闭浏览器


if __name__ == "__main__":
    unittest.main()