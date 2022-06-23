'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-23 15:47:57
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 15:56:43
FilePath: \Python_learning_Core_code\Day003\HWork06.py
Description: 找出100-999之间的水仙花数
~ 153 = 1^3 + 5^3 + 3^3

~ 百位: 123 // 100 = 1 ---> 23
  十位: 123 //10 ---> 12 % 10 ---> 2
        123 % 100 ---> 23 // 10 ---> 2
  个位: 123 % 10 = 12 ---> 3
~ 百位: 567 // 100 = 5 ---> 67
  十位：
  个位: 567 % 10 = 56 ---> 7

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

for num in range(100, 1000):
    low = num % 10 # 个位
    mid = num // 10 % 10 # 十位
    high = num // 100 # 百位
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

