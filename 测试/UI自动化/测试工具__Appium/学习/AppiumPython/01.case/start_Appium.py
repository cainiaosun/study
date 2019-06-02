from appium import webdriver

capabilities={
  "platformName": "Android",
  "deviceName": "127.0.0.1:21503",
  #"app": "C:\\Users\\孙洪斌\\Downloads\\逍遥安卓下载\\mukewang_7090.apk",
  "appPackage":"cn.com.open.mooc",
  "appActivity":"com.imooc.component.imoocmain.splash.MCSplashActivity",
  #"noReset": "true"
}

webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)