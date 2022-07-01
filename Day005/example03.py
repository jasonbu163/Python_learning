'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-30 18:13:30
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-01 18:27:22
FilePath: \Python_learning_Core_code\Day005\example03.py
Description: 列表的遍历 (把每个元素一次取出来)

~ 索引运算(下标运算) - 通过正向或者负向索引获取元素

~ len() ---> length ---> 给出列表中有多少个元素

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

nums = [35, 98, 12, 27, 66]
nums.pop()
nums.append(78)
nums.append(45)

# print(nums[0], nums[-5])
# print(nums[2], nums[-3])
# print(nums[4], nums[-1])  

# nums[2] = 120

# print(nums)

# 对列表进行读操作的for循环
# for num in nums:
#     print(num)
#     x = 100
# print(nums)

# 先通过enumerate函数对列表进行预处理
# 循环遍历的时候既可以获取到索引 (下标) 又可以获取到元素
for i, x in enumerate(nums):
    print(i, x)

# 对列表进行读写操作的for循环
# for i in range(len(nums)):
#     print(i, nums[i])
#     nums[i] = 100
# print(nums)

# for i in range(-5, 0):
#     print(nums[i])