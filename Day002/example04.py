'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-16 22:49:38
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-20 17:00:09
FilePath: \Python_learning_Core_code\Day002\example04.py
Description: 赋值运算符和符合赋值运算符
~ 赋值运算符：右边赋值给左边（变量） --->  = 
~ 算术运算符 --->  + - * / // % **
~ 符合的算术运算符 --->  += -= *= /= //= %= **=
~ 关系运算符（比较运算符） --->  > < >= <= == != 
~ 逻辑运算符：把多个布尔值处理成一个布尔值（做多个布尔值的组合） --->  and（与） / or（或） / not（非）

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

a = 10
b = 3
a += b      # 相当于：a = a + b
a *= a + 2  # 相当于：a = a * (a + 2)
# Python中没有a++这种写法
print(a)

print('--------------------------------')

print(a > b)
print(a != b)
print(a <= b)

print('--------------------------------')

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('--------------------------------')

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print('--------------------------------')

print(not True)
print(not False)