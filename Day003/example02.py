'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-17 16:09:40
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-17 16:32:25
FilePath: \Python_learning_Core_code\Day003\example02.py
Description: 
    分段函数求值
               3x - 5 (x > 1)
        f(x) = x + 2 (-1 <= x <= 1)
               5x + 3 (x < -1)

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''


#例1

x = float(input('x = '))

if x > 1:
    y = 3 * x - 5
elif x >= -1 or x <= 1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))


 #例2

x = float(input('x = '))

if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x +3
print('f(%.2f) = %.2f' % (x, y))
