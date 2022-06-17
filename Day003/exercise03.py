'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-05-24 15:48:30
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-17 16:35:30
FilePath: \Python_learning_Core_code\Day003\exercise03.py
Description: 判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print('三角形的周长：%f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('三角形的面积：%f' % (area))
else:
    print('输入的a,b,c不能构成三角形！！！')