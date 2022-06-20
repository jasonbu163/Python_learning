'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-16 22:49:38
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-17 16:30:39
FilePath: \Python_learning_Core_code\Day002\exercise03.py
Description: 输入年份 如果是闰年输出True 否则输出False

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

year = int(input('请输入年份：'))
# 如果代码太长写一行不便于阅读 可以使用\对代码进行折行
is_leap = year % 4 == 0 and year % 100 != 0 or \
    year % 400 == 0
print(is_leap)