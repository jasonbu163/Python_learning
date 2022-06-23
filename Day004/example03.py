'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-05-25 10:38:03
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 21:35:09
FilePath: \Python_learning_Core_code\Day004\example03.py
Description: 数字矩阵
输入N，按照如下所示的规律进行打印
N = 5
1
2 2
3 3 3
4 4 4 4 
5 5 5 5 5

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

N = int(input('N = '))

for i in range(1, N + 1) :
    for _ in range(1, i + 1):
        print(i, end=' ') 
    print() 