'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-23 11:42:58
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 12:07:44
FilePath: \Python_learning_Core_code\Day003\example05.py
Description: 
~ 用for循环实现1~100求和
~ 用for循环实现1~100之间的偶数求和

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

print('用for循环实现1~100求和')
total = 0
for x in range(1, 101):
    # sum = sum + x
    total += x
print(total)
print('-' * 10)


print('用for循环实现1~100之间的偶数求和')
#range(1，101)中实际范围是1~100，并不会取到101

print('-----我的答案-----')
total = 100
for x in range(100, 0, -2):
    total += x
print(total)

print('-----答案1（这个效率高，运行了50次）-----')
total = 100
for x in range(2, 101, 2):
    total += x
print(total)

print('-----答案2（这个只是美观，实际上运行了100次）-----')
total = 100
for x in range(1, 101):
    # 在求奇数的时候 if i % 2 （用了布尔值的方法）相当于 if i % 2 != 0 ，建议用后者，考虑代码可读性
    if x % 2 == 0:
        total += x
    else:
        # 没想好可以用pass
        pass
print(total)


print('-----使用sum（）函数求和效果一样-----')
i = sum(range(1, 101))
print(i)