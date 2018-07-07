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

print '-------------------------------默认参数知识点---------------------------------------'
"""    
1.无论有多少默认参数,都是必须参数在前
2.无论有多少默认参数,若不传入默认参数值,则使用默认值
3.若要更改某一个默认参数值,又不想传入其他默认参数,企鹅该默认参数的位置不是第一个,这可以通过参数吗更改想要更改的默认参数值
4.若有一个默认参数通过传入参数名更改参数值,则其他想要更改的默认参数都需要传入参数名更改参数值,否则报错。
5.更改默认参数值时,传入默认参数的顺序不需要根据定义的函数中的默认参数的顺序传入,不过最好同时传入参数名,否则容易出现执行结果与预期不一致的情况。
"""

print '----------------------------可变参数--------------------------------------------'
print '----------使用*args，同时包含一个必须的参数-----------------------------------------------'
def test_args(first, *args):
   print 'Required argument: ', first
   for v in args:
      print 'Optional argument: ', v

test_args(1, 2, 3, 4)

print '--------------使用*kwargs, 同时包含一个必须的参数和*args列表------------------------------'
def test_kwargs(first, *args, **kwargs):
   print 'Required argument: ', first
   for v in args:
      print 'Optional argument (*args): ', v
   for k, v in kwargs.items():
      print 'Optional argument %s (*kwargs): %s' % (k, v)

test_kwargs(1, 2, 3, 4, k1=5, k2=6)


print '--------------------------------------------'
# # Use *args
# args = [1, 2, 3, 4, 5]
# test_args(*args)
#
# # Use **kwargs
# kwargs = {
#     'first': 1,
#     'second': 2,
#     'third': 3,
#     'fourth': 4,
#     'fifth': 5
# }
#
# test_args(**kwargs)


print '------------------ 匿名函数 lambda()--------------------------------'
"""
lambda这个名称来自于LISP，而LISP则是从lambda calculus(一种符号逻辑形式)取这个名称的。 
在Python中，lambda作为一个关键字，作为引入表达式的语法。想比较def函数，lambda是单一的表达式，而不是语句块!

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

语法 
lambda 函数的语法只包含一个语句，如下：

lambda [arg1 [,arg2,.....argn]]:expression

#  lambda 参数列表：return [表达式] 变量
#  由于lambda返回的是函数对象（构建的是一个函数对象），所以需要定义一个变量去接收

优点
使用Python写一些脚本时，使用lambda可以省去定义函数的过程，让代码更加精简。
对于一些抽象的，不会被别的地方再重复使用的函数，有时候函数起个名字也是个难题，使用lambda不需要考虑命名的问题
使用lambda在某些时候然后代码更容易理解
"""
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print  "相加后的值为 : ", sum( 10, 20 ) # 相加后的值为 :  30
print  "相加后的值为 : ", sum( 20, 20 ) # 相加后的值为 :  40

infors = [{"name":"wang","age":10},{"name":"xiaoming","age":20},{"name":"banzhang","age":10}]

infors.sort(key=lambda x:x['age']) #根据age对字典排序

print(infors)

# 把lambda当一个变量
def test(a,b,func):
    result = func(a,b)
    return result


num = test(11,22,lambda x,y:x+y)
print(num)


print('-----------------------------递归函数-------------------------------------------------')
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print '----调用递归函数执行的结果为: ---',fact(5)


def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num - 1,num * product)

print '运行fact(5)的结果为:',fact_iter(5,1) # fact(5)