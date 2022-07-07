'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-07-07 19:02:23
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-07 19:03:31
FilePath: \Python_learning_Core_code\Day006\example10.py
Description: 幸运的女人(Josephu环)

有15个男人和15个女人坐船出海, 船坏了, 需要把其中15个人人到海里, 其他人才能活下来;
所有人围成一圈, 由某个人从1开始一次报数, 报到9的人被扔到海里, 下一个人重新从1开始报数,
直到将15个人扔到海里。最后, 15个女人都幸存了下来, 15个男人都被扔到了海里。
问原先哪些位置是男人, 哪些位置是女人。

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

persons = [i for i in range(1, 31)]
for _ in range(15):
    persons = persons[9:] + persons[:8]
for i in range(1, 31):
    print('女' if i in persons else '男', end='')