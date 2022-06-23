'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-23 21:16:42
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 21:35:56
FilePath: \Python_learning_Core_code\Day004\example02.py
Description: 打印出1-100范围内的质数

~ 嵌套循环

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

for num in range(2, 100):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')

print()
# 我的答案
from math import sqrt

for num in range(2,100):
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print(num, end=' ')
print()