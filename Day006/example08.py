'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-07-07 12:25:35
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-07 16:32:09
FilePath: \Python_learning_Core_code\Day006\example08.py
Description: 随机抽取和乱序

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

import random


names = [
    '徐芯言', '侯韧怀', '乔蓓芯', '薄轲德', '汪炯啸', '华滔竹', '仲韶兵', '詹雍广', 
    '侯方宙', '滕蒙淳', '怀正湛', '宋芮宝', '宁珑媚', '任炯苹', '焦融闽', '咎田劲', 
    '尹月妮', '柳杰斐', '劳千真', '叶牧昊', '毕臣焘', '骆秋或', '幸品定', '武晴恬', 
    '许露霏', '陶珣芳', '龙念悦', '骆原韶', '夏心海', '贡娇依', '成旭栋', '郝锬宗', 
    '焦静冶', '雷飞雨', '翟宁楚'
]
print(len(names))
# sample函数可以对列表元素进行无放回抽样
print(random.sample(names, 5))
# choices函数可以对列表元素进行有放回抽样(可以重复抽中)
print(random.choices(names, k=5))
# choice函数可以从列表中随机选择一个元素
print(random.choice(names))
# shuffle函数可以实现列表元素的随机乱序
random.shuffle(names)
print(names)