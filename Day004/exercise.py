# 输入一个正整数判断是不是素数
""" 
from math import sqrt

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
 """


# 输入两个正整数，计算他们的最大公约数和最小公倍数
""" 
x = int(input('x = '))
y = int(input('y = '))

if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
 """
""" 
# C语言中改过来的答案
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
 """

#  打印三角形图案
# 不往print()这中填入任何参数则为换行
from msilib.schema import RadioButton


row = int(input('请输入行数：'))
for i in range(row):
    for _ in range(i + 1):
        print('*', end = '')
    print()

print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end = '')
        else:
            print('*', end = '')
    print()

print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end = '')
    for _ in range(2 * i + 1):
        print('*', end = '')
    print()