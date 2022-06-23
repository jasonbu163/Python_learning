'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-23 21:38:48
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 21:43:14
FilePath: \Python_learning_Core_code\Day004\example04.py
Description: 输出乘法口诀表

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j} * {i} = {i * j}', end='\t')
    print()