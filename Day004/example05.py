'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-23 23:05:28
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 23:08:52
FilePath: \Python_learning_Core_code\Day004\example05.py
Description: 成斐波那契数列

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''
n = int(input('n = '))

a, b = 1, 1
print(a, b, sep='\n')
for _ in range(2, n):
    a, b = b , a + b
    print(b)

print('-----生成斐波那契数列的前20个数-----')
# 生成斐波那契数列的前20个数

# 我的答案
f1, f2 = 1, 1
print(f1)
print(f2)
for _ in range(18):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f3)

print('-' * 10)

# 大佬的答案
a = 0
b = 1
for _ in range(20):
    a, b = b, a+b
    print(a, end=' ')
print()
