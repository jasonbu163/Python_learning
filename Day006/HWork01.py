'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-07-07 19:11:48
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-07 19:42:10
FilePath: \Python_learning_Core_code\Day006\HWork01.py
Description: 

用一个列表保存54张扑克牌, 先洗牌,
再按斗地主的发牌方式把牌发给三个玩家, 多的3张牌给第一个玩家(地主),
最后把每个玩家手上的牌显示出来。

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''
import random


suites = ['♠', '♥', '♣', '♦']
faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards = [f'{suite}{face}' for suite in suites for face in faces]
# cards = []
# for suite in suites:
#     for face in faces:
#         cards.append(f'{suite}{face}')
cards.append('大王')
cards.append('小王')
# 洗牌
random.shuffle(cards)
# 发牌
player_one = []
player_two = []
player_three = []
for _ in range(17):
    player_one.append(cards.pop())
    player_two.append(cards.pop())
    player_three.append(cards.pop())
# 把地主牌给玩家一
# player_one.extend(cards)
player_one += cards
# 手牌排序
player_one.sort(key=lambda x: x[2:])
player_two.sort(key=lambda x: x[2:])
player_three.sort(key=lambda x: x[2:])
# 显示玩家手牌
for card in player_one:
    print(card, end=' ')
print()
for card in player_two:
    print(card, end=' ')
print()
for card in player_three:
    print(card, end=' ')
print()

