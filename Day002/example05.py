'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-16 22:49:38
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-20 17:07:54
FilePath: \Python_learning_Core_code\Day002\example05.py
Description: 比较运算符和逻辑运算符的使用
~ and和or两个运算符有短路功能，因此也被称为短路运算符

短路运算符就是从左到右的运算中前者满足要求，就不再执行后者了； 可以理解为：

    &&为取假运算，从左到右依次判断，如果遇到一个假值，就返回假值，以后不再执行，否则返回最后一个真值；

    || 为取真运算，从左到右依次判断，如果遇到一个真值，就返回真值，以后不再执行，否则返回最后一个假值。

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)
print('flag1 =', flag1)
print('flag2 =', flag2)
print('flag3 =', flag3)
print('flag4 =', flag4)
print('flag5 =', flag5)

print('-----------------------------')

a = int(input('a = '))
flag1 = a > 50
flag2 = a % 2 == 0

print(flag1, flag2)
print(flag1 and flag2)
print(a > 50 and a % 2 == 0)