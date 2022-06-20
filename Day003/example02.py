'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-17 16:09:40
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-20 18:53:37
FilePath: \Python_learning_Core_code\Day003\example02.py
Description: 
    分段函数求值 ---> 如何构造多个分支
               3x - 5 (x > 1)
        f(x) = x + 2 (-1 <= x <= 1)
               5x + 3 (x < -1)

~ 分支结构可以嵌套使用，但是一定要注意嵌套的深度，嵌套深度太深直接影响代码的可读性

~ 代码块：保持相同缩进的代码就属于同一个代码块

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

#写法1（这种写法更扁平，代码越扁平越好，可读性越高）
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'f({x:.2f}) = {y:.2f}')


 #写法2
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x +3
print(f'f({x:.2f}) = {y:.2f}')
