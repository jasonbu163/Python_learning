'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-23 16:08:49
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 16:26:44
FilePath: \Python_learning_Core_code\Day003\HWork07.py
Description: 输入两个非负整数m和n(m >= n), 计算C(m,n)的值
~ A(m, n) = m! / (m - n)! ---> 排列 ---> permutation
~ C(m, n) = m! / n! / (m - n)! ---> 组合 ---> combination

~ C(5, 3) = 5! / 3! / 2! = 10

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

# 笨重的写法
""" 
m = int(input('m = '))
n = int(input('n = '))

fm = 1
for i in range(2, m + 1):
    fm *= i

fn = 1
for i in range(2, n + 1):
    fn *= i

fm_n = 1
for i in range(2, m - n + 1):
    fm_n *= i

print(fm // fn // fm_n)
 """

# 有更简洁的写法
from math import factorial as f
# 从math模块导入factorial函数并改成别名f
# as ---> alias ---> 别名

m = int(input('m = '))
n = int(input('n = '))

print(f(m) // f(n) // f(m - n))