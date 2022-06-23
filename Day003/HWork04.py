'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-23 12:17:13
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 15:45:46
FilePath: \Python_learning_Core_code\Day003\HWork04.py
Description: 输入一个正整数判断是不是素数(只能被1和自身整除的数)

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''
from math import sqrt


num = int(input('请输入一个正整数：'))
end = int(sqrt(num))

is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num, end=' or ')
    print(f'{num}是质数')
else:
    print('%d不是素数' % num, end=' or ')
    print(f'{num}不是质数')
 