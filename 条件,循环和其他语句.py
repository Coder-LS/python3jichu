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
Date:2018/6/21
QQ:1217750958
"""
__author__ = 'LS'

#python import 自己的包
print '------------------------------------python import 自己的包\n----------------------------------------'
""" 
 1.自己写的包放到哪里？

1
2
3
>>> import sys
>>> sys.path
['', '/usr/lib64/python34.zip', '/usr/lib64/python3.4', '/usr/lib64/python3.4/plat-linux', '/usr/lib64/python3.4/lib-dynload', 
'/usr/lib64/python3.4/site-packages', '/usr/lib/python3.4/site-packages']
　可以看到上面列举了一些文件夹地址，那么自己写的包理论上都可以放到上述地址中，但有一些如”/usr/lib64/python3.4“并不推荐，比较推荐的是：“” , 
“'/usr/lib/python3.4/site-packages'”, “'/usr/lib64/python3.4/site-packages'”

 

2.如何导入自己写的包？

比如“/usr/lib/python3.4/site-packages”，如果我写了 一个 exp.py 文件放在这个文件下，那么我在自己的系统写的 python3 文件都可以采用 import exp 导入。

  还可以看到还有一个是“”，及当前文件夹，假如 存在如此的 一个 文件 结构：

1         parent/
2                   one/<br>　　　　　　　　　__init__.py
3                        exp.py
4                        exp2.py
5                   exp3.py
parent/
        one/<br>　　　　　　　　　__init__.py
            exp.py
            exp2.py
        exp3.py
　　exp.py和exp2.py都在one目录下，那么在exp2.py中可以通过 import exp 导入exp.py

　　而exp3.py和one都处在parent目录下，那么在exp3.py中可以通过 import one.exp 导入exp.py

 

3.__init__.py的作用

　　偶尔可以看到有些人写的包下面还会有一个__init__.py，它的作用是在导入包时首先执行的。

　　假设在 exp3.py 中写入 import one.exp ，那么会首先执行 __init__.py 文件，接着会执行exp.py文件

　　如果不需要，__init__.py可以为空，也可以干脆不加入__init__.py

 

4.if __name__ == "__main__"

　　也有时候会看到 .if __name__ == "__main__" 语句，它的作用就是当此文件没有被作为导入的文件使用时执行 if 语句块里的程序。

　　假如 exp.py 中加入了 if __name__ == "__main__" ，然后 python3 exp.py，就会执行这个语句块里的内容

　　而 如果 if __name__ == "exp"，时则是被 其他文件 以 "import exp"导入时执行的部分

　　有如果是 if __name__ == "one.exp"，时则是被 其他文件 以 "import one.exp"导入时执行的部分

　　注意 在  "import exp"时是不会执行 if __name__ == "one.exp"中的内容的！同样： "import one.exp“是不会执行 if __name__ == "exp"中的内容的
 """

# python 断言 assert（）
print '-----------------------------------------------python 断言 assert（）\n\n-----------------------------------------------------'
"""   
 使用assert断言是学习python一个非常好的习惯，python assert 断言句语格式及用法很简单。在没完善一个程序之前，我们不知道程序在哪里会出错，
 与其让它在运行最崩溃，不如在出现错误条件时就崩溃，这时候就需要assert断言的帮助。本文主要是讲assert断言的基础知识。

python assert断言的作用

python assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假。可以理解assert断言语句为raise-if-not，
用来测试表示式，其返回值为假，就会触发异常。

assert断言语句的语法格式

    assert python 怎么用？
    expression assert 表达式
1  assert语句用来声明某个条件是真的。
2  如果你非常确信某个你使用的列表中至少有一个元素，而你想要检验这一点，并且在它非真的时候引发一个错误，那么assert语句是应用在这种情形下的理想语句。
3  当assert语句失败的时候，会引发一AssertionError。
 """

# assert 1==1
# assert 1 == 2


# assert 2+2==2*2
# assert len(['my boy',12])<10
# assert range(4)==[0,1,2,3]
# mylist = ['item']
# assert len(mylist) >= 1
# mylist.pop()
# assert len(mylist) >= 1
"""     
如何为assert断言语句添加异常参数

assert的异常参数，其实就是在断言表达式后添加字符串信息，用来解释断言并更好的知道是哪里出了问题。格式如下：

1    assert expression [, arguments]
2    assert 表达式 [, 参数]
"""

""""
print '--------------------------------------assert函数 自定异常\n--------------------------------------------------------------------'

class ShortInputException(Exception):
    '''自定义的异常类'''
    def __init__(self, length, atleast):
        #super().__init__()
        self.length = length
        self.atleast = atleast

def main():
    try:
        s = input('请输入 --> ')
        if len(s) < 3:
            # raise引发一个你定义的异常
            raise ShortInputException(len(s), 3)
    except ShortInputException as result:#x这个变量被绑定到了错误的实例
        print('ShortInputException: 输入的长度是 %d,长度至少应是 %d'% (result.length, result.atleast))
    else:
        print('没有异常发生.')

main()

"""

print '------------------------------------------------循环遍历字典元素\n-------------------------------------------------------'
print ' ------1.对键和值都进行遍历------'
d = {'name1' : 'pythontab', 'name2' : '.', 'name3' : 'com'}
for key, value in d.items():
    print (key, ' value : ', value)

print '-------2.迭代-------------------'
#判断str是否可迭代
from collections import Iterable #如何判断一个对象是否可迭代，通过collections模块的Iterable类型判断

print '判断\'ABC\'是否属于可迭代的对象  :',isinstance('ABC',Iterable)
print '判断123是否属于可迭代的对象    :',isinstance(123,Iterable)
L = {1,2,3,4}
T = ('A','B','C','D')
D = {1:'A',2:'B',3:'C',4:'D'}
S = {"name","age","sex","adress"}
print '判断list是否属于可迭代的对象   :' ,isinstance(L,Iterable)
print '判断tuple是否属于可迭代的对象  :',isinstance(T,Iterable)
print '判断dict是否属于可迭代的对象   :' ,isinstance(D,Iterable)
print '判断set是否属于可迭代的对象    :' ,isinstance(S,Iterable)

print '--------3.Python3 enumerate() 函数------------------'
"""   
描述
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

语法
以下是 enumerate() 方法的语法:

enumerate(sequence, [start=0])
参数
sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置。
返回值
返回 enumerate(枚举) 对象。
"""

for index,value in enumerate(['first','second','third']):
    print(index,":",value)
print("上面是list，下面是dict")
for index,key in enumerate({'first':1,'second':2,'third':3}):
    print(index,":",key)
'''
for index,value in enumerate(('first','second','third')):
	print(index,":",value)
'''#当然tuple，字符串等都是可以的，只要满足可迭代，就可以这样写

print '-------4.并行迭代--------------------'
names = ['anne','beth','george','damon']
ages = [12,45,32,102]
for i in range(len(names)):
    print(names[i],'is',ages[i],'years old')

print '----------------------------------------'
zip(names,ages)

print '----------------------------------------'

for name,age in zip(names,ages):
    print(name,'is',age,'year old')

print '----------------------------------------'
for name,age,number in zip(names,ages,range(4)):
    print(number,':',name,'is',age,'year old')

