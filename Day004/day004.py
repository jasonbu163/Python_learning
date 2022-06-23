'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-05-25 09:24:03
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 11:51:32
FilePath: \Python_learning_Core_code\Day004\day004.py
Description: 

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''





#  猜数字游戏
""" 
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了！！！')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足！！！')
 """

#  输出乘法口诀表(九九表)
""" 
for i in range(1, 10):
    for j in range(1, i+1):
        print('%d*%d=%d' % (j, i, i * j), end = '\t')
    print()
 """