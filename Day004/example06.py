'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-23 23:11:58
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 23:31:49
FilePath: \Python_learning_Core_code\Day004\example06.py
Description: 百钱百鸡
~ 鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？

~ 穷举法: 穷尽所有的可能性,让后设置条件,找到问题的解 ---> 暴力破解法

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

print('假设公鸡5块一只、母鸡3块一只、小鸡1块三只, 100块可以买100只鸡有哪些方案', end='\n\n')

""" 
for x in range(0, 21):
    for y in range(0, 34):
        for z in range(0, 100, 3):
            if x + y + z == 100 and 5 * x + 3 * y + z // 3 == 100:
                print('100块钱可以买到公鸡%d只、母鸡%d只、小鸡%d只。' % (x, y, z))
"""               
# 优化
for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            print('100块钱可以买到公鸡%d只、母鸡%d只、小鸡%d只。' % (x, y, z))