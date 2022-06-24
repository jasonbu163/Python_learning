'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-23 23:40:12
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-24 20:29:35
FilePath: \Python_learning_Core_code\Day004\example07.py
Description: 五人捕鱼

A、B、C、D、E 五人在某天夜里合伙去捕鱼，到第二天凌晨时都疲惫不堪，于是各自找地方睡觉。

日上三杆, A 第一个醒来，他将鱼分为五份，把多余的一条鱼扔掉，拿走自己的一份。

B 第二个醒来，也将鱼分为五份，把多余的一条鱼扔掉拿走自己的一份。

C、D、E依次醒来, 也按同样的方法拿鱼。

问他们至少捕了多少条鱼?

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''
fish = 6
while True:
    is_enough = True

    # 检查目前的鱼的数量够不够五个人分
    total = fish
    for _ in range(5):
        if (total - 1) % 5 == 0:
           total = (total - 1) // 5 * 4
        else:
            is_enough = False
            break

    if is_enough:
        print(fish)
        break
    fish += 5 