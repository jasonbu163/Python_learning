'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-30 17:49:29
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-01 18:30:25
FilePath: \Python_learning_Core_code\Day005\example02.py
Description: 容器型数据类型(用一个变量可以保存多个数据)

~ 列表 (list) ---> 
~ 元组 (tuple)
~ 集合 (set)
~ 字典 (dict)

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

# 创建列表的字面量语法
# num = [] # 空列表
nums = [10, 100, 1000, 1.23, ] # 尽量放同一种元素
print(type(nums))
print(nums)

rules = ['热爱祖国，热爱人民', '尊敬师长，团结同学', 
         '好好学习，天天向上', '保护公共财物，不得在公共区域大声喧哗'
]
print(type(rules))
print(rules)

# 追加元素 (把元素加到列表的末尾)
nums.append(10000)
# 插入元素 (在指定的位置加入元素)
nums.insert(0, 1)
print(nums)

# 删除元素 (默认删除最后一个元素)
rules.pop()
rules.pop()
print(rules)
