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



# 序列相加
print '-------------------------------序列相加----------------------------------------------------'
a = [1,2,'hellow']
b = ['world',3,4]
print (a+b)

# python转义字符 （如 \n ) +  字符串格式化符号 ( 如 %d ）

#  字符串 符号,对齐和0填充
print '-------------------------------字符串 符号,对齐和0填充------------------------------------------'
print ('圆周率的PI的值为: %010.2f'%3.141593)  # 标表

print ('圆周率的PI的值为: %10.2f'%3.14)
# 减号（-）用来左对齐数值
print ('圆周率的PI的值为: %-10.2f'%3.14)       # 右侧为多出的空格

# 对齐正负号
print ( ( '%5d' % 10 ) + '\n' + ( '%5d' % - 10))
print ( ( '宽度前加加号: % + 5d' % 10) + '\n' + ('宽度前加加号：% + 5d' % - 10))

# 字符串 translate()方法
print '--------------------------字符串方法------------------------------------------------------'
"""
语法
translate()方法语法：

str.translate(table[, deletechars]);
参数
table -- 翻译表，翻译表是通过maketrans方法转换而来。
deletechars -- 字符串中要过滤的字符列表。
返回值
返回翻译后的字符串。
"""

from string import maketrans

intab = 'adfas'
outtab = '12345'
trantab = maketrans(intab,outtab)
st = 'just do it'
print 'st 调用 tdanslate 方法后：',st.translate(trantab)  # 字符串乱码问题  如果加了括号之后


# 字典方法  fromkeys()
print '--------------------------字典方法------------------------------------------------------'

"""
描述
Python 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。

语法
fromkeys()方法语法：

dict.fromkeys(seq[, value])
参数
seq -- 字典键值列表。
value -- 可选参数, 设置键序列（seq）的值。
返回值
该方法返回一个新字典。
"""
# seq = ('name','age','sex')
# indo = dict.fromkeys(seq,10)
# print ("新字典为: %s"%   info)



seq = ('Google', 'Runoob', 'Taobao')

dict = dict.fromkeys(seq)
print "新字典为 : %s" % str(dict)

dict = dict.fromkeys(seq, 10)
print "新字典为 : %s" % str(dict)

# 字典方法 items()
"""
描述
Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组。

语法
items()方法语法：

dict.items()
参数
NA。
返回值
返回可遍历的(键, 值) 元组数组。
"""
dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}

print "字典值 : %s" % dict.items()

# 遍历字典列表
for key, values in dict.items():
    print key, values


# 字典方法 setdefault（）
"""
Python 字典(Dictionary) setdefault()方法
描述
Python 字典 setdefault() 函数和get() 方法类似, 如果键不存在于字典中，将会添加键并将值设为默认值。

语法
setdefault()方法语法：

dict.setdefault(key, default=None)
参数
key -- 查找的键值。
default -- 键不存在时，设置的默认键值。
返回值
如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值。
"""
# !/usr/bin/python
# -*- coding: UTF-8 -*-

dict = {'baidu': '百度', 'google': 'Google 搜索'}

print "Value : %s" % dict.setdefault('baidu', None)
print "Value : %s" % dict.setdefault('Taobao', '淘宝')