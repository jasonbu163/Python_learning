'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-07-04 17:15:55
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-04 17:31:38
FilePath: \Python_learning_Core_code\Day006\example05.py
Description: 列表的操作(反转和排序)

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

items = ['banana', 'grape', 'apple', 'waxberry', 'pitaya', 'apple']

# 反转
items.reverse()
print(items)

# 排序 ---> 可以修改reverse参数控制排升序或者排降序: items.sort(reverse=True)
items.sort()
print(items)

nums = ['1', '10', '234', '2', '35', '100']
nums.sort(key=int)
print(nums)
# nums2 = [int(num) for num in nums]
# nums2.sort()
# nums3 = [str(num) for num in nums2]
# print(nums3)