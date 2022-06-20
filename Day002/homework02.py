'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-16 22:49:38
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-17 16:30:17
FilePath: \Python_learning_Core_code\Day002\exercise02.py
Description: 输入元的半径计算周长和面积

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

# 我的答案

r = float(input('请输入圆的半径：'))
pi = 3.1416
d = pi * r * 2
S = pi * r * r
print(f'圆的周长为：{d:.2f}')
print('圆的面积为：%.2f' % S)

# 老师的答案

radius = float(input('请输入圆的半径：'))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)
