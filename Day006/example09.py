'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-07-07 16:35:51
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-07 16:50:41
FilePath: \Python_learning_Core_code\Day006\example09.py
Description: 幸运的女人(Josephu环)

有15个男人和15个女人坐船出海, 船坏了, 需要把其中15个人人到海里, 其他人才能活下来;
所有人围成一圈, 由某个人从1开始一次报数, 报到9的人被扔到海里, 下一个人重新从1开始报数,
直到将15个人扔到海里。最后, 15个女人都幸存了下来, 15个男人都被扔到了海里。
问原先哪些位置是男人, 哪些位置是女人。

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

persons = [True] * 30
index, counter, number = 0, 0, 0
while counter < 15:
    if persons[index]:
        number += 1
        if number == 9:
            persons[index] = False
            counter += 1
            number = 0
    index += 1
    if index == 30:
        index = 0
for person in persons:
    # 三元条件运算 ---> if后面的表达式为True, 取if前面的的值, 否则取else后面的值
    # 相当于简写版(精简版)的if...else...结构
    print('女' if person else '男', end='')

