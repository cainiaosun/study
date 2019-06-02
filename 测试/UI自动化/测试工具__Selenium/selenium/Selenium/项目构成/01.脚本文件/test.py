import unittest, time , datetime , re,os,sys
sys.path.append(".//")
sys.path.append(sys.path[0].split("项目构成")[0] + '项目构成\\02.方法模块')
#import Function_temp as F,ATQ案例执行页面 as P
content='停止执行，错误信息：定位错误：中文字幕组1000中文字幕组+11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112222222222222222222222222222221'
if len(content.split('：',1))>1:
	reson=content.split('：',1)[0]
	temp_content=content.split('：',1)[1]
	content=temp_content

#print(text)
#print(content)
#F.pop_up_box(text)

class pop():
	def __init__(self):
		self.content=content
	def newline(self,string,length=60):
		string="      "+self.content
		for i in range(0,1000):
			if i==0:
				text="错误信息："
			elif byte_length(string)>length:
				for j in range(0,1000):
					if byte_length(string[0:j])>=length:
						if i==1:
							text=text+"\n"+string[0:j+6]
							string=string[j+6:len(string)]
							break
						text=text+"\n"+string[0:j]
						string=string[j:len(string)]
						break
			else:
				text=text+"\n"+string+"\n详细错误信息请见：日志目录"
				break
		return text

	def byte_length(self,str):
		str=self.content
		length=len(str)
		utf_8_length=len(str.encode('utf-8'))
		byte_length=int((utf_8_length-length)/2+length)
		return byte_length
'''
print(content)
print(F.content(content))
F.pop_up_box(content)
'''
class test():
	def __init__(self,a):
		self.a=a
	def re(self):
		return self.a
	def sum(self,b,a=""):
		if self.a!="":
			a=self.a
		return a+b

number=1
def sum(a):
	try:
		return int(a)
	except:
		next(a)

def next(a):
	eval("sum")(a)



#print(my())
#print(sum("sdsad"))

def add_lol(fun):
	def decorator():
		print("欢迎来到英雄联盟，")
		fun()
	return decorator

@add_lol
def lol():
	print("敌军还有6s钟到达战场")

lol()



def cool(func):
	def add_world(*args,**kwargs):
		return func(name,country)+",welcom to here!"	
	return add_world

#@cool
def hello(name="sunhongbin",country="English"):
	print("locals is:"+str(locals()))
	return country+","+name+",hello"



#inspect.getmembers
#str=inspect.getargspec(f).__code__.co_argcount
print(dir(hello))
print(hello.__defaults__)
print(hello.__code__.co_varnames)
print(hello.__code__.co_argcount)
'''
def myhello(hello.__code__.co_varnames):
	print("this is locals:"+str(locals()))
	return country+","+name+",hello"
print(myhello(country="china",name="xiaohua"))
'''
exec("name"+'=%d'%15)

print(name)

print(type(name))

kwargs={"name":"sunhongbin"}

def kw(**kwargs):
	print("kw name:"+str(name))
	print("kw locals():"+str(locals()))

#kw()

print(hello(country=""))

def entrace(fun):
		def decotor(*args,**kwargs):
			try:
				print("entrace locals:"+str(locals()))
				#print(str(fun.__code__.co_varnames))
				return fun(*args,**kwargs)
			except Exception as e:
				return fun.__name__+":"+str(repr(e))
		return decotor

class myclass():
	@entrace
	def fun1(self,a=10,b=20):
		s=a+b+1
		return s

	@entrace
	def fun2(self,c):
		return c+1


print(myclass().fun1())



def local(a,b,*m,c=0,**p):
	print(locals())

#local(a=10,b=20,m=(20,40))
#
#
#dic={'kwargs': {'b': 1, 'a': 12}, 'args': "11", 'fun': "22"}
#sdic=dic['kwargs']
#print(str(sdic))
t=(1,2,3)
print(t[1:3])
t=t[1:]
print(t)


import traceback
class myclass1():
	def entrace1(fun):
		def decotor(*args,**kwargs):
			try:
				print("entrace locals:"+str(locals()))
				myfun=locals()["fun"]
				#print(str(fun.__code__.co_varnames))
				return myfun(*args,**kwargs)
			except Exception as e:
				print("trace is:"+str(traceback.print_exc()))
				print("trace_f is:"+str(traceback.format_exc()))
				return fun.__name__+":"+str(repr(e))
		return decotor

	@entrace1
	def fun1(self,a=10,b=20):
		s=a+b+1
		return s

	@entrace1
	def fun2(self,c):
		return c+1
#print(myclass1.__defaults__)
print("dir："+str(dir(myclass1)))
print(myclass1().__module__)
instance=myclass1()
test=getattr(instance,"fun1")
print(str(dir(instance)))
strclass=str(instance.__class__).split(".")
classname=strclass[len(strclass)-1].split("'")[0]
print("class is:"+str(instance.__class__))
print("delattr is:"+str(instance.__delattr__))
print("getattribute is:"+str(instance.__getattribute__))
print(test("str"))

print("1\n2\n")

处理异常
重新执行，错误信息：find_element.find_element：NoSuchElementException('Unable to locate element: [name="loginId1"]', None, None)
处理异常
重新执行，错误信息：find_element.find_element：NoSuchElementException('Unable to locate element: [name="loginId1"]', None, None)
处理异常
跳过操作，错误信息：find_element.find_element：NoSuchElementException('Unable to locate element: [name="loginId1"]', None, None)
.处理异常
重新执行，错误信息：find_element.find_element：NoSuchElementException('Unable to locate element: [name="loginId1"]', None, None)
处理异常
停止执行，错误信息：find_element.find_element：NoSuchElementException('Unable to locate element: [name="loginId1"]', None, None)
E
======================================================================
ERROR: test_20_entrace (__main__.ATQtest)
----------------------------------------------------------------------


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 41, in decorator
    return fun(*args,**kwargs)
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 210, in find_element
    return driver.find_element(locator[0], locator[1])
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 955, in find_element
    'value': value})['value']
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 312, in execute
    self.error_handler.check_response(response)
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [name="loginId1"]


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 18, in check_decorator
    element=instance.find_element()
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 53, in decorator
    next_step(instance,fun.__name__,error,detail_error,*args,**kwargs)
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 74, in next_step
    getattr(instance,name)(*args,**kwargs)
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 53, in decorator
    next_step(instance,fun.__name__,error,detail_error,*args,**kwargs)
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 79, in next_step
    raise Exception(detail_error)
Exception: traceback.format_exc:
Traceback (most recent call last):
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 41, in decorator
    return fun(*args,**kwargs)
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 210, in find_element
    return driver.find_element(locator[0], locator[1])
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 955, in find_element
    'value': value})['value']
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 312, in execute
    self.error_handler.check_response(response)
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [name="loginId1"]


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 41, in decorator
    return fun(*args,**kwargs)
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 210, in find_element
    return driver.find_element(locator[0], locator[1])
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 955, in find_element
    'value': value})['value']
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 312, in execute
    self.error_handler.check_response(response)
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [name="loginId1"]



During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\01.脚本文件\测试脚本.py", line 141, in test_20_entrace
    element=F.find_element(P.用户名输入框).click_on(1,2)
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 25, in check_decorator
    raise Exception(detail_error)
Exception: traceback.format_exc:
Traceback (most recent call last):
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 41, in decorator
    return fun(*args,**kwargs)
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 210, in find_element
    return driver.find_element(locator[0], locator[1])
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 955, in find_element
    'value': value})['value']
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 312, in execute
    self.error_handler.check_response(response)
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [name="loginId1"]


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 41, in decorator
    return fun(*args,**kwargs)
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 210, in find_element
    return driver.find_element(locator[0], locator[1])
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 955, in find_element
    'value': value})['value']
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 312, in execute
    self.error_handler.check_response(response)
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [name="loginId1"]


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 18, in check_decorator
    element=instance.find_element()
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 53, in decorator
    next_step(instance,fun.__name__,error,detail_error,*args,**kwargs)
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 74, in next_step
    getattr(instance,name)(*args,**kwargs)
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 53, in decorator
    next_step(instance,fun.__name__,error,detail_error,*args,**kwargs)
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 79, in next_step
    raise Exception(detail_error)
Exception: traceback.format_exc:
Traceback (most recent call last):
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 41, in decorator
    return fun(*args,**kwargs)
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 210, in find_element
    return driver.find_element(locator[0], locator[1])
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 955, in find_element
    'value': value})['value']
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 312, in execute
    self.error_handler.check_response(response)
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [name="loginId1"]


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 41, in decorator
    return fun(*args,**kwargs)
  File "C:\Users\Pactera\Desktop\学习文件\selenium\Selenium\项目构成\02.方法模块\Function_temp.py", line 210, in find_element
    return driver.find_element(locator[0], locator[1])
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 955, in find_element
    'value': value})['value']
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 312, in execute
    self.error_handler.check_response(response)
  File "E:\InstallSoftWare\python3.6\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [name="loginId1"]




----------------------------------------------------------------------
Ran 2 tests in 54.112s

FAILED (errors=1)
