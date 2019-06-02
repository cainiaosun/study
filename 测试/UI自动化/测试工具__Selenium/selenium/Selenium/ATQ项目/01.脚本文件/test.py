import unittest, time , datetime , re,os,sys
sys.path.append(".//")
sys.path.append(sys.path[0].split("ATQ项目")[0] + 'ATQ项目\\02.方法模块')
import Function_temp as F
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


#print(myclass().fun1())



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
#print("class is:"+str(instance.__class__))
#print("delattr is:"+str(instance.__delattr__))
#print("getattribute is:"+str(instance.__getattribute__))
#print(test("str"))

'''
1.能不能访问函数的变量和子方法、子类，如同访问类属性一样 
  答案：函数下的变量、方法、包括嵌套的子类均不能访问，只能在函数内部起作用，如下例子：
'''
def fun():
  a=10
  global g
  g=20
  def child_fun():
    print("这是fun函数的子函数child_fun！")
    print("父函数变量a的值是："+str(a))#在子函数中可以直接访问父函数的变量
  class child_class:
    def child_class_fun():
      print("这是fun函数的子类child_class下的child_class_fun函数!")
      print("父函数变量a的值是："+str(a))#在子类中可以直接访问父函数的变量
  child_fun()#在函数内部可以使用子函数
  child_class.child_class_fun()#在函数内部可以使用子类的子函数
fun()#函数调用，可以观察到上方变量及函数、类间的相互访问
#使用如下方式打印出fun函数及函数实例的属性，并没有诸如a、g、child_fun、child_class等属性，
#故而如fun.a、fun().a等访问函数变量和子方法均会报错
print(dir(fun))
print(dir(fun()))

''' 
2.嵌套类中，父类访问子类属性以及子类访问父类属性
  答案：子类、父类之间属性访问同访问外部类相似：类名.属性、实例.属性，不能直接调用，
        但是类不能直接调用自身和自身实例
'''

class parent(object):  
  a=10
  def __init__(self):
    self.b=15
  def child_func1(self):
    print()
  def child_func2():
    return outer().m
  #print(fun())
  class child(object):
    b=50
    def fun():
      print(outer.a+outer().m+outer.fun1()+10)
'''
print(outer.a)
outer().inner.fun()
print(dir(outer))
print(dir(outer()))
print(dir(outer.inner()))      

def a():
  def b():
    print(1000)
  class c(object):
    """docstring for ClassName"""
    def m():
      print("这是类！")
      '''
      
'''
1.类简要介绍
'''
#类的定义方法
class parent(object):
  a=100#类变量
  def __init__(self, arg):
    super(parent, self).__init__()
    self.arg = arg#实例变量

  #下面两种写法的静态方法
  #没有用装饰器装饰的静态方法只能通过类访问，如果通过实例对象访问会传入self作为参数导致报错
  def func1():
    return "这是一个类的普通静态方法func1"

  @staticmethod
  #使用了装饰器装饰的静态方法，可以通过类和实例对象访问，实例对象访问也不传入self参数
  def func2():
    return "这是一个装饰器形成的静态方法func2！"

  
  @classmethod
  #使用了装饰器形成的类方法，只能通过类访问，类会将本身作为参数传入，如下会将本身传入函数参数cls中；
  #实例对象访问就会报错（实例对象访问会把类本身以及self对象都传入参数，导致多一个参数报错）
  def func3(cls):
    return "这是一个装饰器形成的类方法func3！"

  
  @property
  #装饰器伪装方法形成的类成员变量，需使用实例对象访问，如果使用类访问返回是一个属性对象
  def func4(self):
    return "这是一个装饰器形成的类字段func4！"

  @property
  #装饰器伪装方法形成的类成员变量，需使用实例对象访问，如果使用类访问返回是一个属性对象
  def func5(self):
    return "这是一个成员方法func5！"

print("类                                  ："+str(parent))
print("类实例对象                           ："+str(parent(100)))
print("如下是类的属性列表："+str(dir(parent)))
print(parent(100).__dict__)

print("通过类访问没有用装饰器的静态方法       ："+str(parent.func1()))
#print("通过类实例对象访问没有用装饰器的静态方法："+str(parent(10).func1()))
print("通过类实例对象访问装饰器形成的类方法    ："+"类实例对象访问装饰器形成的类方法会报错！")

print("通过类访问装饰器形成的静态方法         ："+str(parent.func2()))
print("通过类实例对象访问装饰器形成的静态方法  ："+str(parent(10).func2()))

print("通过类访问装饰器形成的类方法           ："+str(parent.func3()))
#print("通过类实例对象访问装饰器形成的类方法："+str(parent(10).func3()))
print("通过类实例对象访问装饰器形成的类方法    ："+"类实例对象访问装饰器形成的类方法会报错！")

print("通过类访问装饰器伪装的成员变量         ："+str(parent.func4))
print("通过类实例对象访问装饰器伪装的成员变量  ："+str(parent(10).func4))

print("通过类实例对象访问成员方法  ："+str(parent(10).func5))



class mmm(object):
  def papa(self):
    print(self)

  @classmethod
  def gaga(cls):
    print(cls)

print(mmm())
mmm().papa()
print(mmm)
mmm.gaga()

def en(func):
  def de(*args,**kwargs):
    print(args)
    print(kwargs)
    #func(*args,**kwargs)
  return de




class rokie(object):
  def min(self):
    pass

print("公成员的全部属性")

def mage():
  pass

ob=rokie()
length=len(dir(ob))
for i in range(0,length):
  print(dir(ob)[i]+":"+str(eval("ob."+dir(ob)[i])))

ob=rokie
length=len(dir(ob))
for i in range(0,length):
  print(dir(ob)[i]+":"+str(eval("ob."+dir(ob)[i])))

print(type(rokie))
print(type(rokie()))
print(type(mage))
print(type(mage()))

print(isinstance(rokie,rokie))

print(type(F.find_element(1212)))

i=[1,2,3]
if "__self__" in dir(rokie().min):
  print("yes")
else:
  print("no")


class ruke(object):
  @staticmethod
  def my(b,c):
    print("yes")

  def ceshi(self):
    pass


ob=ruke.my(1,3)
name=ruke.my.__qualname__
print(name)
print(ruke().my)
print("打印全部属性")

def mumu():
	ruke.my(1,2)
	print(ruke.my)
mumu()