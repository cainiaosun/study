from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()#设置对象
        self.driver.implicitly_wait(30)
        self.base_url = "http://11.8.127.248:8080/atq/frame.jsp"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver=self.driver
        username = 'sunhongbin'
        driver.get(self.base_url)
        driver.find_element_by_name('loginId').clear()
        driver.find_element_by_name('loginId').send_keys(username)
        driver.find_element_by_name('password').send_keys('123456')
        driver.find_element_by_link_text('登录').click()
        #等待
        time.sleep(2)
        aa=driver.find_element_by_xpath("//a/span")
        aa.find_element_by_xpath("//span[contains(text(),'执行管理')]").click()
        #切换iframe页面
        xf=self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/div/iframe")
        driver.switch_to.frame(xf)
        s = self.pop_up_box()#手工输入获取需求名称，不带日期也可以，但是最好还是带日期，以免存在重复的需求名称
        for i in range(1,4):
            #通过拼接字符串是实现find_element的变量输入，contains()和text()方法
            if i==1:
               ss=s+"（第一轮）"
            elif i==2:
                ss = s+"（第二轮）"
            else:
                ss = s+"（回归测试）"
            driver.find_element_by_xpath("//span[contains(text(),'"+ss+"')]").click()
            #查找父元素..,查找弟弟元素following-sibling::tr[1]，[1]里面的1表示最近的一个（第一个）弟弟元素，\在行指代换行
            driver.find_element_by_xpath("//span[contains(text(),'"+ss+"')]\
            /../../../following-sibling::tr[1]//span[text()='孙洪斌']").click()
            #实例化Select并选择
            s1=Select(driver.find_element_by_id("stat"))
            s1.select_by_index(1)
            driver.find_element_by_xpath("//a[@id='']/span/span[text()='查询']").click()
            time.sleep(5)
            for j in range(1, 500):
                #Keys类模拟键盘发送空格键
                if self.isElementExist("by_xpath","/html/body/div[3]/div/div/div/div[2]/div[1]/div[2]/div/table/\
                tbody/tr[1]/td[2]/div/input")==False:
                    break
                driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div[1]/div[2]/div/table/\
                tbody/tr[1]/td[2]/div/input").send_keys(Keys.SPACE)
                driver.find_element_by_xpath("//span[text()='执行分配案例']").click()
                time.sleep(2)
                #回到主frame页
                driver.switch_to.default_content()
                s2=Select(driver.find_element_by_id("allstat"))
                s2.select_by_index(1)
                time.sleep(2)
                driver.find_element_by_xpath("//span[text()='保存']").click()
                time.sleep(2)
                driver.switch_to.frame(xf)

        #self.driver.find_element_by_xpath("//div[@id='line']/span[2]/a[4]/span/span/span").click()
        #self.driver.switch_to.alert().accept()
        time.sleep(20)



    # 弹出一个窗口并返回输入的值
    def pop_up_box(self):
        import tkinter
        def input():
            try:
                root.destroy()
            except:
                num = "异常处理！"

        def inputclear():
            var.set('')

        root = tkinter.Tk()
        root.title("输入框")
        root.geometry("250x130")

        l1 = tkinter.Label(root, text='请输入需求名称')
        l1.pack()
        var = tkinter.StringVar()
        var.set("")
        entry1 = tkinter.Entry(root, textvariable=var)
        entry1.pack()
        btn1 = tkinter.Button(root, text="提交", command=input)
        btn2 = tkinter.Button(root, text="清空", command=inputclear)
        btn2.pack(side='right')
        btn1.pack(side='right')
        root.mainloop()
        return var.get()

    def isElementExist(self,by_type,element):
        flag=True
        driver=self.driver
        try:
            if by_type=="by_xpath":
                driver.find_element_by_xpath(element)
            elif by_type=="by_id":
                driver.find_element_by_id(element)
            elif by_type=="by_name":
                driver.find_element_by_name(element)
            elif by_type=="by_css":
                driver.find_element_by_css_selector(element)
            return flag
        except:
            flag=False
            return flag

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()