'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-23 12:05:52
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 15:44:27
FilePath: \Python_learning_Core_code\Day003\example07.py
Description: 输入两个正整数，计算他们的最大公约数和最小公倍数

~ 最大公约数（greatest common divisor）

~ bug ---> 缺陷 / 故障 /问题 ---> debug（调试）

~ mobilize / demobilize
  modem ---> moderate / demoderate
  encode / decode
  
Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

x = int(input('x = '))
y = int(input('y = '))

if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break

print('-' * 10)

# C语言中改过来的答案
# example08.py中有改进代码
x = int(input('x = '))
y = int(input('y = '))

if y > x:
    # x，y大数在前并保存在a，b
    x, y = y, x
    b, a = x, y
while x % y != 0:
    # 辗转相除法求最大公约数
    temp = x
    x = y
    y = temp % y
    if x % y == 0:
        break
print('%d和%d的最大公约数是%d' % (a, b, y))
print('%d和%d的最小公倍数是%d' % (a, b, a * b / y))