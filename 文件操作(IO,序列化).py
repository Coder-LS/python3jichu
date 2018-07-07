# usr/bin/python3
# -*- coding: utf-8 -*-
# /**
#  *                    _ooOoo_
#  *                   o8888888o
#  *                   88" . "88
#  *                   (| -_- |)
#  *                    O\ = /O
#  *                ____/`---'\____
#  *              .   ' \\| |// `.
#  *               / \\||| : |||// \
#  *             / _||||| -:- |||||- \
#  *               | | \\\ - /// | |
#  *             | \_| ''\---/'' | |
#  *              \ .-\__ `-` ___/-. /
#  *           ___`. .' /--.--\ `. . __
#  *        ."" '< `.___\_<|>_/___.' >'"".
#  *       | | : `- \`.;`\ _ /`;.`/ - ` : | |
#  *         \ \ `-. \_ __\ /__ _/ .-` / /
#  * ======`-.____`-.___\_____/___.-`____.-'======
#  *                    `=---='
#  *
#  * .............................................
#  *          佛祖保佑             永无BUG
#  */

"""
Project:LS  
Date:2018/6/23
QQ:1217750958
"""
__author__ = 'LS'

"""
    I/O编程中,数据流。input 从外面（磁盘，网络）流进内存，output是从内存流到外面去。
"""



"""
序列化和反序列化

在运行程序的过程中，所有变量都在内存中，我们把变从内存中变量成可存储的或可传输的过程称为序列化。
我们可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。反之，把变量内容从序列化的对象重新读到内存里称为反序列化。

序列化是指将数据结构或对象转换成二进制的过程。
反序列化是指将序列化过程中生成的二进制串转换成数据结构或对象的过程。

我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
将对象转换为可通过网络传输或可以存储到本地磁盘的数据格式（如：XML、JSON或特定格式的字节串）的过程称为序列化；反之，则称为反序列化。

"""

print '----------------------------------------pickle序列化-----------------------------------------------'

import pickle
d = dict(name = 'xiao zhi' , num = 1002)
print (pickle.dumps(d))     # pickle.dumps()方法把任意对象序列化为bytes，然后把其写入文件。pickle.dump()直接把对象写入文件。
c = pickle.dumps(d)
print (pickle.loads(c))                  # 同理 loads 和 load  反序列化

print '----------------------------------------json序列化-----------------------------------------------'

"""
Python转JSON

Python	JSON
dict	Object
list, tuple	array
str	string
int, float, int- & float-derived Enums	numbers
True	true
False	false
None	null

JSON转Python

JSON	Python
object	dict
array	list
string	str
number(int)	int
number(real)	float
true	True
false	False
null	None


说明：

Python dict中的非字符串key被转换成JSON字符串时都会被转换为小写字符串；
Python中的tuple，在序列化时会被转换为array，但是反序列化时，array会被转化为list；
由以上两点可知，当Python对象中包含tuple数据或者包含dict，且dict中存在非字符串的key时，反序列化后得到的结果与原来的Python对象是不一致的；
对于Python内置的数据类型（如：str, unicode, int, float, bool, None, list, tuple, dict）json模块可以直接进行序列化/反序列化处理；
对于自定义类的对象进行序列化和反序列化时，需要我们自己定义一个方法来完成定义object和dict之间进行转化。


"""
# Python对象变成一个JSON：
# （dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。）
import json
d = dict(name='Bob', age=20, score=88)
print json.dumps(d)

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
#　反序列化得到的所有字符串对象默认都是unicode而不是str。由于JSON标准规定JSON编码是UTF-8，
# 所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。
c = json.dumps(d)
print json.loads(c)

print '-------------------------------------------------JSON进阶-Student类实例序列化为JSON--------------------------'
class Student(object):
   def __init__(self, name, age, sex):
      self.name = name
      self.age = age
      self.sex = sex
   def s_obj(self,s):
     return {'name':self.name, 'age':self.age, 'sex':self.sex}

s = Student('lsy', 23, 'girl')
print json.dumps(s, default=s.s_obj)

"""
JSON进阶
Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s))
运行代码，毫不留情地得到一个TypeError：

Traceback (most recent call last):
  ...
TypeError: <__main__.Student object at 0x10aabef50> is not JSON serializable
错误的原因是Student对象不是一个可序列化为JSON的对象。

如果连class的实例对象都无法序列化为JSON，这肯定不合理！

别急，我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数：

https://docs.python.org/2/library/json.html#json.dumps

这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。

可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(s, default=student2dict))
这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON。

不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：

print(json.dumps(s, default=lambda obj: obj.__dict__))
因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。

同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
运行结果如下：

<__main__.Student object at 0x10cd3c190>
打印出的是反序列化的Student实例对象。
"""