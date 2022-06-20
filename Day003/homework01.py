'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-17 16:34:14
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-20 17:54:15
FilePath: \Python_learning_Core_code\Day003\homework01.py
Description: 英制单位英寸和公制单位厘米互换

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

value = float(input('请输入长度：'))
unit = input('请输入单位：')

if unit == 'in' or unit == '英寸':
    print('%.2f英寸 = %.2f厘米' % (value, value * 2.54))
    print(f'{value:.2f}英寸 = {value * 2.54:.2f}厘米')
elif unit == 'cm' or unit == '厘米':
    print('%.2f厘米 = %.2f英寸' % (value, value / 2.54))
    print(f'{value:.2f}厘米 = {value / 2.54:.2f}英寸')
else:
    print('请输入有效的单位')