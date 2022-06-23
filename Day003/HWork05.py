'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-23 12:17:53
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 12:18:09
FilePath: \Python_learning_Core_code\Day003\HWork05.py
Description: 打印三角形图案

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''
 
# 不往print()这中填入任何参数则为换行
from msilib.schema import RadioButton


row = int(input('请输入行数：'))
for i in range(row):
    for _ in range(i + 1):
        print('*', end = '')
    print()

print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end = '')
        else:
            print('*', end = '')
    print()

print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end = '')
    for _ in range(2 * i + 1):
        print('*', end = '')
    print()