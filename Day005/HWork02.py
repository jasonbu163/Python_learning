'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-07-01 21:46:11
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-01 23:21:49
FilePath: \Python_learning_Core_code\Day005\HWork02.py
Description: 向列表中添加10个随机整数,找出其中第2大的元素

~ [a, b) ---> random.random() * (b - a) + a ---> 如果要包括b的话(b - a)要改成(b - a + 1)
 
~ 取0-100的小数: temp = random.random() * 100
~ 取100-200的小数: temp = random.random() * 100 + 100

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

import random


# 先生成10个随机整数

# nums = []
# for _ in range(10):
#     nums.append(random.randrange(1, 100))

# 列表的生成式语法 (推导式) ---> 写法简明, 效率更高
nums = [random.randrange(1, 100) for _ in range(10)]

print(nums)

# # 方法一
# # 先找到nums中最大值
# max_value = max(nums)
# # 然后删除最大值
# # 通过remove操作从列表中删除指定的元素
# nums.remove(max_value)
# # 最后再次找到的最大值为原来nums数组中的第二大值
# print(max(nums))

# 方法二
# nums = [35, 12, 99, 99, 57, 99, 57, 35, 54]
m1, m2 = nums[0], nums[1]
if m1 < m2:
    m1, m2 = m2, m1
for i in range(2, len(nums)):
    if nums[i]  > m1:
        m1, m2 = nums[i], m1
    # 当你遇到和最大值一样大的值, 就用pass或者continue跳过(如果逻辑为重复的数只取一个为最大时)
    elif nums[i] == m1:
        pass
    elif nums[i] > m2:
        m2 = nums[i]
# print(m1, m2)
print(m2)

# 在一个列表中放上1-100的数
nums = [i for i in range(1, 101)]
print(nums)
# 在一个列表中放上1-100的j奇数数
nums = [i for i in range(1, 101, 2)]
print(nums)