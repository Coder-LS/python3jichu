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
Date:2018/6/22
QQ:1217750958
"""
__author__ = 'LS'

print '-----------------------------------类的构造方法------------------------------------------------------------------'
# first example
class MyClass(object):
    i = 123
    def __init__(self,name):
        self.name = name

    def f(self):
        return 'hellow,' + self.name

use_class = MyClass('xiaoming')
print '调用类的属性；', use_class.i
print '调用类的方法:', use_class.f()

"""
在Python中,__init__()方法会在对象实例化时被调用。(initialization初始化)
先输入两个下划线+init+两个下划线,构造方法。在定义类时,若不显示地定义一个__init__()方法,则程序默认调用一个无参。
"""
# second example
class DefaultInit(object):
    def __init__(self):
        print '\n类实例化时执行我,我是__init__方法。'

    def show(self):
        print '我是类中定义的方法，需要通过实例化对象调用。'

test = DefaultInit()
print '类实例化结束。'
test.show()

# third example
class DefaultInit(object):
    def show(self):
        print '我是类中定义的方法,需要通过实例化对象调用。'

test = DefaultInit()
print '\n类实例化结束。'
test.show()

"""   
代码中定义了__init__()方法时,实例化会调用。若没有会调用默认的__init__()方法。
__init__()方法可以有参数,参数通过__init__()方法传递到类的实例化操作上。
"""

# fourth example

class DefaultInit():
    def __init__(self):
        print '\n我是不带参数的__init__()方法.'

DefaultInit()
print '类实例化结束。'

# five example
class DefaultInit():
    def __init__(self):
        print '\n我是不带参数的__init__()方法.'

    def __init__(self , param):            #  覆盖
        print '\n我是一个带参数的__init__方法，参数值为：', param

DefaultInit('hellow')
print '类的实例化结束。'

""" 
一个类中可以定义多个构造方法，但实例化类时只实例化最后偶的构造方法，即覆盖前面的构造方法，
并且还根据最后一个构造方法的形参进行实例化。建议一个类只定义一个构造法方法。
"""
print '-----------------------------------类的访问权限------------------------------------------'

"""在类内部有属性和方法，外部代码可以通过直接调用实例变量的方法操作数据，隐藏了内部的复杂逻辑"""
class Student(object):
    def __init__(self , name , score):
        self.name = name
        self.score = score

    def info(self):
        print '学生： %s ;  分数 : %s' % (self.name , self.score)

stu = Student('xiaoming',95)
print '修改前的分数：', stu.score
stu.info()
stu.score=0
print '修改后的分数：', stu.score
stu.info()

print '-------------内部属性变为私有变量--------------------------------------------'
"""  
内部属性前加两个下划线变为私有变量,只有内部能访问，所以下面程序的score不能从外部访问了，会出错
"""
# class Student(object):
#     def __init__(self , name , score):
#         self.__name = name
#         self.__score = score
#
#     def info(self):
#         print '学生： %s ;  分数 : %s' % (self.__name , self.__score)
#
# stu = Student('xiaoming',95)
# print '修改前的分数：', stu.__score
# stu.info()
# stu.__score=0
# print '修改后的分数：', stu.__score
# stu.info()

print '-----------get_attrs方法获取类中私有变量---------------------'

class Student(object):
    def __init__(self , name , score):
        self.__name = name
        self.__score = score

    def info(self):
        print '学生： %s ;  分数 : %s' % (self.__name , self.__score)

    def get_score(self):
        return self.__score


stu = Student('xiaoming',95)
print '修改前的分数：', stu.get_score()
stu.info()
stu.__score=0
print '修改后的分数：', stu.get_score()
stu.info()

""" 
同理 set_attrs 可以修改类中的私有变量 ( set_score(0) )，set方法可以帮助做参数检查，避免穿入无效参数

"""

print '-----------------私有方法----------------------------------'

class PrivatePublicMethod(object):
    def __init__(self):
        pass

    def __foo(self):             # 私有方法
        print '这是私有方法'

    def foo(self):               # 公共方法
        print '这是公共方法。'
        print '公共方法中调动私有方法'
        self.__foo()
        print '公共方法调用私有方法结束'

pri_pub = PrivatePublicMethod()
print '开始调用公共方法：'
pri_pub.foo()
print '开始调用私有方法：'
#pri_pub.__foo()                #  错误

"""出错  AttributeError: 'PrivatePublicMethod' object has no attribute '__foo'
   私有方法和私有变量相似,不能通过外部调用。
"""

print '------------------------------------继承-------------------------------------------------------------------------'

"""
代码重用，实现方法之一就是继承，即类之间类型和子类型的关系。
定义一个class时，可以从现有的某个class继承，定义为子类（Subclass），被继承的为基类,父类或超类（Base class，Super class）。
需要注意：继承语法的class子类名（基类名）时，//基类名写在括号里，基类是在定义类时，在元组中指明的。

1.在继承中，基类的构造方法（__init__()方法）不会自动被调用，需要在子类的构造方法中专门调用
2.在调用基类的方法时需要加上基类的类名前缀，并带上self参数变量。区别与于类中调用普通函数是不需要带self参数
3.在Python中，首先查找对应类型的方法，如果在子类中找不到对应的方法，才到基类中逐个查找

子类不能调用父类的私有方法
"""


class Person(object):  # 定义一个父类

    def talk(self):  # 父类中的方法
        print("person is talking....")


class Chinese(Person):  # 定义一个子类， 继承Person类

    def walk(self):  # 在子类中定义其自身的方法
        print('is walking...')


c = Chinese()
c.talk()  # 调用继承的Person类的方法
c.walk()  # 调用本身的方法

# 输出

print '----------------构造函数的继承----------------------------------------------'
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 'weight'

    def talk(self):
        print("person is talking....")


class Chinese(Person):

    def __init__(self, name, age, language):  # 先继承，在重构
        Person.__init__(self, name, age)  # 继承父类的构造方法，也可以写成：super(Chinese,self).__init__(name,age)
        self.language = language  # 定义类的本身属性

    def walk(self):
        print('is walking...')


class American(Person):
    pass


c = Chinese('bigberg', 22, 'Chinese')

"""如果我们只是简单的在子类Chinese中定义一个构造函数，其实就是在重构。这样子类就不能继承父类的属性了。
所以我们在定义子类的构造函数时，要先继承再构造，这样我们也能获取父类的属性了。

      子类构造函数基础父类构造函数过程如下：

      实例化对象c ----> c 调用子类__init__()  ---- > 子类__init__()继承父类__init__()  ----- > 调用父类 __init__()
      """


# class SchoolMember(object):
#     '''学习成员基类'''
#     member = 0
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.enroll()
#
#     def enroll(self):
#         '注册'
#         print('\njust enrolled a new school member [%s].' % self.name)
#         SchoolMember.member += 1
#
#     def tell(self):
#         print('----%s----' % self.name)
#         for k, v in self.__dict__.items():
#             print(k, v)
#         print('----end-----')
#
#     def __del__(self):
#         print('开除了[%s]' % self.name)
#         SchoolMember.member -= 1
#
#
# class Teacher(SchoolMember):
#     '教师'
#
#     def __init__(self, name, age, sex, salary, course):
#         SchoolMember.__init__(self, name, age, sex)
#         self.salary = salary
#         self.course = course
#
#     def teaching(self):
#         print('Teacher [%s] is teaching [%s]' % (self.name, self.course))
#
#
# class Student(SchoolMember):
#     '学生'
#
#     def __init__(self, name, age, sex, course, tuition):
#         SchoolMember.__init__(self, name, age, sex)
#         self.course = course
#         self.tuition = tuition
#         self.amount = 0
#
#     def pay_tuition(self, amount):
#         print('student [%s] has just paied [%s]' % (self.name, amount))
#         self.amount += amount
#
#
# t1 = Teacher('Wusir', 28, 'M', 3000, 'python')
# t1.tell()
# s1 = Student('haitao', 38, 'M', 'python', 30000)
# s1.tell()
# s2 = Student('lichuang', 12, 'M', 'python', 11000)
# print(SchoolMember.member)
# del s2
#
# print(SchoolMember.member)


print '------------------------------------------多态，封装，多重继承-------------------------------------------------'

"""
多态

当子类存在于父类相同的方法时，会覆盖父类的方法，在代码运行时总会调用子类方法。
isinstance（a ，list）  判断a是不是list类型
或 isinstance（a ，Animal）  判断a是不是Animal类中的

多态的意思是：对于一个变量，我们只需要他是Animal'类型，无须确切地知道它的子类型，就可以放心的调用run()方法。具体调用run()
方法作用于哪个对象，有运行时该对象的确切类型决定。
调用只管调用，不管细节。
开闭原则： 开放开展新Animal子类，不需要修改依赖于父类的run_two_times()函数。
"""
class Animal(object):
    def run(self):
        print 'Animal is running.........'

class Dog(Animal):
    def run(self):
        print 'Dog is running...........'

class Cat(Animal):
    def run(self):
        print 'Cat is running...........'


def run_two_times(animal):
    animal.run()
    animal.run()

run_two_times(Animal())
run_two_times(Dog())
run_two_times(Cat())


"""
封装

在程序设计中，封装（Encapsulation）是对具体对象的一种抽象，即将某些部分隐藏起来，在程序外部看不到，其
含义是其他程序无法调用。要了解封装，离不开“私有化”，就是将类或者是函数中的某些属性限制在某个区域之内，外部无法调用。
在编程语言里，对外提供的接口（接口可理解为了一个入口），就是函数，称为接口函数，
这与接口的概念还不一样，接口代表一组接口函数的集合体。

第一个层面的封装（什么都不用做）：创建类和对象会分别创建二者的名称空间，我们只能用类名.或者obj.的方式去
访问里面的名字，这本身就是一种封装。
注意：对于这一层面的封装（隐藏），类名.和实例名.就是访问隐藏属性的接口
第二个层面的封装：类中把某些属性和方法隐藏起来(或者说定义成私有的 __)，只在类的内部使用、外部无法访问，或
者留下少量接口（函数）供外部访问。
类中所有双下划线开头的名称如__x都会自动变形成：_类名__x的形式：

property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值（就是一个装饰器）
　　注意：被property装饰的属性会优先于对象的属性被使用，而被propery装饰的属性,
分成三种：property、被装饰的函数名.setter、被装饰的函数名.deleter（都是以装饰器的形式）。
将一个类的函数定义成特性以后，对象再去使用的时候obj.name,根本无法察觉自己的name是执行了一个函数然后
计算出来的，这种特性的使用方式遵循了统一访问的原则。

"""
#类的设计者
class room: #定义一个房间的类
    def __init__(self,name,owner,length,width,high):
        self.name = name
        self.owner = owner
        self.__length = length #房间的长
        self.__width = width #房间的宽
        self.__high = high #房间的高
    @property
    def area(self): #求房间的平方的功能
        return self.__length * self.__width #对外提供的接口，隐藏了内部的实现细节，\
                                            # 此时我们想求的是房间的面积就是：长x宽

#类的使用者
r1 = room("客厅","michael",20,30,9) #实例化一个对象r1
print(r1.area) #通过接口使用（area），使用者得到了客厅的面积


#类的设计者，轻松的扩展了功能，而类的使用者完全不需要改变自己的代码
class room: #定义一个房间的类
    def __init__(self,name,owner,length,width,high):
        self.name = name #房间名
        self.owner = owner #房子的主人
        self.__length = length #房间的长
        self.__width = width #房间的宽
        self.__high = high #房间的高
    @property
    def area(self): #对外提供的接口，隐藏内部实现
        return self.__length * self.__width,\
               self.__length * self.__width * self.__high #此时我们增加了求体积,
        # 内部逻辑变了,只需增加这行代码就能简单实现,而且外部调用感知不到,仍然使
        # 用该方法，但是功能已经增加了

#类的使用者
r1 = room("客厅","michael",20,30,9) #实例化一个对象r1
print(r1.area) #通过接口使用（area），使用者得到了客厅的面积

print '------------------------------------------异常处理---------------------------------------------------------------'
'''
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生


try:
<语句>
finally:
<语句>    #退出try时总会执行
raise
使用 raise 语句抛出一个指定的异常
raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。

'''