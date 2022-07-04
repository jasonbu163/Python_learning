'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-07-04 12:08:58
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-04 17:09:51
FilePath: \Python_learning_Core_code\Day006\example03.py
Description: 列表的相关操作

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

# print(ord('e'))
# print(ord('o'))
# print('zealous' < 'zoo')
# print(ord('王'))
# print(ord('骆'))
# print('王大锤' < '骆昊')

# items1 = ['banana', 'grape', 'apple', 'waxberry', 'pitaya']
# items2 = ['car', 2, 3, 4]
# print(items1 < items2)

items = ['banana', 'grape', 'apple', 'waxberry', 'pitaya', 'apple']

# index() ---> 查找元素在列表中的索引(下标)
if 'strawberry' in items:
    print(items.index('strawberry'))
if 'apple' in items:
    print(items.index('apple'))
if 'apple' in items[3:]:
    print(items.index('apple', 3))

# count() ---> 统计元素在列表中出现的次数
print(items.count('apple'))
print(items.count('strawberry'))


# 添加元素
items.append('blueberry')
items.insert(1, 'watermelon')
print(items)

# 删除元素
items.pop()
items.pop(4)
del items[0] # 不建议用这种
while 'apple' in items:
    items.remove('apple')
print(items)


# 清空列表元素
items.clear()
print(items)