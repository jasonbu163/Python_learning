'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-07-04 17:40:30
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-06 19:13:14
FilePath: \Python_learning_Core_code\Day006\example06.py
Description: 排序

~ 简单选择排序 - 每次从剩下的元素中选择最小的值

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

nums = [35, 12, 99, 58, 67, 42, 49, 31, 73]

# sorted_nums = []
# while len(nums) > 0:
#     min_value = min(nums)
#     sorted_nums.append(min_value)
#     nums.remove(min_value)
# print(sorted_nums)

# 简单选择排序法
for i in range(len(nums) - 1):
    # 假设第一个元素就是最小值
    min_value, min_index = nums[i], i
    # 通过循环寻找有没有更小的值, 并记下它的位置，从下一位开始
    for j in range(i + 1, len(nums)):
        if nums[j] < min_value:
            min_value, min_index = nums[j], j
    # 将最小的值换到最前面的位置
    nums[i], nums[min_index] = nums[min_index], nums[i]

print(nums)