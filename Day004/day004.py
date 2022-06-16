# 用for循环实现1~100求和
""" 
sum = 0

for x in range(101):
    sum += x
print(sum)
 """

#  用for循环实现1~100之间的偶数求和
#range(1，101)中实际范围是1~100，并不会取到101
""" 
# 我的答案
sum = 100
for x in range(100, 0, -2):
    sum += x
print(sum)

# 答案1
sum = 100
for x in range(2, 101, 2):
    sum += x
print(sum)
# 答案2
sum = 100
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)
 """

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