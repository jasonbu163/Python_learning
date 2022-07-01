'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-07-01 18:52:27
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-01 21:36:17
FilePath: \Python_learning_Core_code\Day005\example05.py
Description: 输入10个整数, 计算平均值、方差、和标准差, 找出最大值和最小值

~ 描述型统计 ---> 通常用于可以获得总体的情况
~ 推断型统计 ---> 只能获得样本, 通过样本去推测总体

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

from statistics import variance

# 输入数据
nums = []
for _ in range(10):
    temp = int(input('请输入数据: '))
    nums.append(temp)
print(nums)

# 平均值
mean_value = sum(nums) / len(nums)

# 方差 ---> variance ---> var 
# ps: 协方差 ---> cov
total = 0
for num in nums:
    total += (num - mean_value) ** 2
var_value = total / (len(nums) - 1)

# 标准差 ---> standard deviation ---> std / stdev
std_var = var_value ** 0.5

# 最大值, 最小值
max_value, min_value = max(nums), min(nums) 

print(f'均值: {mean_value}')
print(f'方差: {var_value}')
print(f'标准差: {std_var}')
print(f'极差(全距): {max_value - min_value}')

