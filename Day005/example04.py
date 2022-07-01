'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-07-01 18:36:19
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-01 18:47:54
FilePath: \Python_learning_Core_code\Day005\example04.py
Description: 将一颗骰子掷60000次,统计出每一面出现的次数

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''
import random

# 列表的重复运算
fs = [0] * 6

for _ in range(60000):
    face = random.randrange(1, 7)
    fs[face - 1] += 1

for i, value in enumerate(fs):
    print(f'{i + 1}点摇出了{value}次')
