'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-07-06 20:27:43
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-06 21:21:26
FilePath: \Python_learning_Core_code\Day006\example07.py
Description: 排序

~ 冒泡排序: 元素两两比较, 如果过前面的元素大于后面的元素, 就交换两个元素的位置

~ [35, 12, 99, 58, 67, 42, 49, 31, 73]
~ 第一趟
1 [12, 35, 99, 58, 67, 42, 49, 31, 73]
2 [12, 35, 99, 58, 67, 42, 49, 31, 73]
3 [12, 35, 58, 99, 67, 42, 49, 31, 73]
4 [12, 35, 58, 67, 99, 42, 49, 31, 73]
5 [12, 35, 58, 67, 42, 99, 49, 31, 73]
6 [12, 35, 58, 67, 42, 49, 99, 31, 73]
7 [12, 35, 58, 67, 42, 49, 31, 99, 73]
8 [12, 35, 58, 67, 42, 49, 31, 73, 99]
~ 第二趟
1 [12, 35, 58, 67, 42, 49, 31, 73 | 99]
2 [12, 35, 58, 67, 42, 49, 31, 73 | 99]
3 [12, 35, 58, 67, 42, 49, 31, 73 | 99]
4 [12, 35, 58, 42, 67, 49, 31, 73 | 99]
5 [12, 35, 58, 42, 49, 67, 31, 73 | 99]
:
:
最终有序

~ 搅拌排序 (鸡尾酒排序)

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''
# nums = [35, 12, 99, 58, 67, 42, 49, 31, 73]
# nums = [9, 1, 2, 3, 4, 5, 6, 7, 8]
nums = [2, 3, 4, 5, 6, 7, 8, 9, 1]

for i in range(1, len(nums)):
    swapped = False
    for j in range(0, len(nums) - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            swapped = True
    if not swapped:
        break

print(nums)