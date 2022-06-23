'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-05-24 15:48:30
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 22:14:37
FilePath: \Python_learning_Core_code\Day003\HWork03.py
Description: 判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

while True:
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        half = perimeter / 2
        area = (half * (half - a) * (half - b) * (half - c)) ** 0.5
        print(f'三角形的周长：{perimeter:.2f}')
        print(f'三角形的面积：{area:.2f}')
        break
    else:
        print('输入的a,b,c不能构成三角形!!!')
        print('请重新输入!!!')
        print('----------------------------------')