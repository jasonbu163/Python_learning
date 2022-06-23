'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-23 12:32:51
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 15:41:14
FilePath: \Python_learning_Core_code\Day003\example08.py
Description: while循环 ---> 不知道循环具体的次数

while 条件:
    print('....')
    print('....')
    print('....')
    修改条件中的变量
    if 条件:
        break
...

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''
i = 0
while i < 10:
    print('hello, world')
    i += 1
print('Game over!')

# example07.py中C语言改进代码
x = int(input('x = '))
y = int(input('y = '))
    
while y % x != 0:
    x, y = y % x , x
print(x)