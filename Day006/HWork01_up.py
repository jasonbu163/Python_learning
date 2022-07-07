'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-07-07 19:11:48
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-07 20:20:59
FilePath: \Python_learning_Core_code\Day006\HWork01_up.py
Description: 

用一个列表保存54张扑克牌, 先洗牌,
再按斗地主的发牌方式把牌发给三个玩家, 多的3张牌给第一个玩家(地主),
最后把每个玩家手上的牌显示出来。

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''
import random

# 创建一副新牌
suites = ['♠', '♥', '♣', '♦']
faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# 列表的生成式(推导式)
cards = [f'{suite}{face}' for suite in suites for face in faces]
# cards = []
# for suite in suites:
#     for face in faces:
#         cards.append(f'{suite}{face}')
# append - 向列表中追加元素
cards.append('大王')
cards.append('小王')
# 随机乱序(洗牌)
random.shuffle(cards)
# 发牌
# players = [[], [], []]
# 嵌套列表(列表中的元素又是列表)
players = [[] for _ in range(3)]

for _ in range(17):
    for player in players:
        # pop - 删除元素(默认删除最后一个元素)
        player.append(cards.pop())
# 把地主牌给玩家一
# extend - 将一个列表的元素合并到另一个列表中
players[0].extend(cards)
# 显示玩家手牌
for player in players:
    # 手牌排序 sort - 对列表中的元素进行排序
    player.sort(key=lambda x: x[1:])
    for card in player:
        print(card, end=' ')
    print()
