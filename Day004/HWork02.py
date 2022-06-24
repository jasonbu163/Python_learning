'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-24 20:53:02
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-24 21:08:16
FilePath: \Python_learning_Core_code\Day004\HWork02.py
Description: 输入10个1-99的整数,计算平均值,找出最大值和最小值

~ Pythonic <---> 跨界程序员

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

total = 0
max_value, min_value = 0, 100

for _ in range(10):
    temp = int(input('请输入：'))
    total += temp
    if temp > max_value:
        max_value = temp
    if temp < min_value:
        min_value = temp
print('-' * 10)
print(f'平均值：{total / 10}')
print(f'最大值：{max_value}')
print(f'最小值：{min_value}')
