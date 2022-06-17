'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-16 22:49:38
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-17 16:30:06
FilePath: \Python_learning_Core_code\Day002\exercise01.py
Description: 将华氏温度转换为摄氏温度

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c)) 
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
