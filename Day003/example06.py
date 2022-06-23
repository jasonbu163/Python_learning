'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-23 12:05:52
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 12:32:06
FilePath: \Python_learning_Core_code\Day003\example06.py
Description: 输出乘法口诀表(九九表)

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''


for i in range(1, 10):
    for j in range(1, i+1):
        print('%d*%d=%d' % (j, i, i * j), end = '\t')
    print()
