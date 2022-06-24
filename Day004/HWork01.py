'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-24 20:31:45
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-24 20:45:37
FilePath: \Python_learning_Core_code\Day004\HWork01.py
Description: 猜数字游戏

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''
import random

answer = random.randrange(1, 101)
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