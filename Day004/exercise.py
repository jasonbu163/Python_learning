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