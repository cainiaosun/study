from selenium import webdriver
import time



#高亮元素    
# @outerentrace(False)
def highlight(driver,id,str1):
    #高亮元素
    element = driver.find_element(id,str1)
    for i in range(5):
        driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", 
            element, "background:withe;border:5px so lid red;") 
        time.sleep(1)
        driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", 
            element, "background:green;border:5px so lid red;") 
        time.sleep(1)


driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
highlight(driver,'id','kw')
highlight(driver,'id','su')
#driver.find_element('id','kw').send_keys("shuru")
#driver.find_element('id','su').click()