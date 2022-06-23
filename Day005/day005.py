#  Craps赌博游戏
# 我们设定玩家开始游戏时有1000元的赌注
# 游戏结束的条件是玩家输光所有的赌注
""" 
from random import randint
# 初始赌注为1000，并且判断是否打空头支票
money = 1000
while money > 0:
    print('你的总资产为：', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
    # 第一轮摇色子
    first = randint(1, 6) + randint(1, 6)
    print('玩家要出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜！')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜！')
        money -= debt
    else:
        # 判断是否需要继续游戏
        needs_go_on = True
    # 继续游戏
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家要出了%d点' % current)
        if current == 7:
            print('庄家胜！')
            money -= debt
        elif current == first:
            print('玩家胜！')
            money += debt
        else:
            needs_go_on = True
print('你破产了，游戏结束！！！')
 """