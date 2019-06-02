#coding=UTF-8
#铺述几个概念：
#列表（list）:使用方括号
list=[1,2,3,4]
print u"列表list打印结果：",list
#元组（tuple）：使用圆括号
tuple=(1,5,3,4)
print u"元组tuple打印结果：",tuple
#字典（dict）：使用大括号：
dict={'num1':1,'num2':2,'num3':3,'numb4':10}
print u"字典dict打印的结果：",dict
####列表、元组、字典都属于序列（序列的两个特点：有索引操作符和切片操作符）



#list的操作
#append(附加):对列表附加新元素
#len:获取列表的长度，通用的方法，可以用在返回很多类型数据的长度
#count:获取某种元素的个数
#extend(扩展):作用可以是把另一个列表并入一个列表中
#index：返回对应的元素首次出现的键值
#pop：移除最后一位并返回，如果是带参数的那么移除对应参数减值的元素并返回
#remove：移除元素，无返回值
#reverse：反向排序
#sort：排序，升序
#sorted：排序升序，可以应用于各个类可排序对象排序
list.append(5)
len=len(list)
count=list.count(1)
list1=[6,7,1]
list.extend(list1)
index=list.index(4)



print u"append方法增加了元素5后的列表：",list
print u"len方法获取新天骄元素后列表的长度：",len
print u"count方法获取的列表中的1元素的个数",count
print u"extend方法扩展的新list列表的打印：",list
print u"index方法获取元素4首次出现的索引",index
pop1=list.pop(4)
print u"pop参数输入4，移除键值为4的元素返回值：",pop1,"新的list：",list
pop2=list.pop()
print u"pop不输入参数，移除最后一位的元素返回值：",pop2,"新的list：",list
list.remove(7)
print u"remove方法移除元素7后的list：",list
list.reverse()
print u"reverse方法反向排序后的list：",list
list.sort()
print u"sort按升序排序后的list：",list
list=sorted(list)
print u"sorted方法升序排序后，重新赋值的list",list



#tuple的操作:tuple是不可变的
#index：返回对应的元素首次出现的键值
#count:获取某种元素的个数
#也能用sorted()和len()函数


dict={'num1':1,'num2':2,'num3':3,'numb4':10}
#dict的操作：字典参数有键和键值
#暂时先补充
list=sorted(dict,reverse=True)
print list




#sorted方法补充专题
#iterable:需要排序的对象
#cmp：
#key：
#reverse:False，True两个值，默认False（生序）
#sorted函数可以对多种对象进行排序，包括:字符串、列表、元组、字典及一些其它数据类型

#对字符串进行排序，返回结果是一个列表
result=sorted("4977665475656")
print u"sorted函数对数字字符串“4977665475656”进行排序：",result
#对列表进行排序，排序后返回一个重新排序后的列表
list=[2,3,4,1,5,9,3,6]
result=sorted(list)
print u"sorted函数排序list列表的结果过：",result
#对元组进行排序，返回值是一个列表
tuple=(2,4,1,5,3,6,9)
result=sorted(tuple)
print u"sorted函数排序tuple元组的结果：",result
#对字典进行排序，返回一个键名组成的列表
dict={'a':1,'f':4,'k':3,'f':87,'d':9,'a':17}
result=sorted(dict)
print u"sorted函数对字典dict进行排序的结果：",result
#reverse参数的使用
result=sorted(list,reverse=True)
print 'reverse参数的使用，True值，降序：',result
#cmp参数的使用
listtem=[('a',1),('b',2),('f',1),('d',3),('e',5)]
result=sorted(listtem,cmp=lambda x,y:cmp(x[0],y[0]))
print result



def comp(x):
    return x["age"]
li=[{"age":32,"name":12},{"age":43,"name":4},{"age":32,"name":11}]
result=comp({"age":32,"name":12})
print result

'''
from operator import itemgetter,attrgetter
sort=['数据4','数据7','数据9','数据4','数据3','数据6','数据100']
sorted(sort)
sort1=[('a',1),('b',2),('f',1),('d',3),('e',5)]
#m=sorted(sort1,key=lambda s:s[0])
#m=sorted(sort1,cmp=lambda x,y:cmp(x[1],y[1]))
#m=sorted(sort1,key=itemgetter(0,1))
sort2={'a':1,"b":2,"f":3,"d":4}
print sort2.iteritems()
print sort2.items()
print itemgetter(1,2)
m=sorted(sort2.iteritems())
print sort2
print m
f=sorted(tuple)
print f
'''



