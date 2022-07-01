'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-07-01 21:38:46
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-01 21:42:27
FilePath: \Python_learning_Core_code\Day005\Hwork01.py
Description: 输入三个整数,按照从大到小的顺序输出

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a < b:
    a, b = b, a

if a < c:
    a, c = c, a

if b < c:
    b, c = c, b

print(a, b, c) 
