'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-05-25 09:24:03
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 21:35:46
FilePath: \Python_learning_Core_code\Day004\example01.py
Description: 

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''
'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-05-25 09:24:03
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 16:04:10
FilePath: \Python_learning_Core_code\Day004\example01.py
Description: 正整数的反转
~ 补充练习: 输入一个正整数N, 将N进行反转
N = 1234
total = 0
1234 // 10 ---> 123 ---> 4
total = total * 10 + 4 
123 // 10 ---> 12 ---> 3
total = total * 10 + 3 ---> 43 
12 // 10 ---> 1 ---> 2
total = total * 10 + 2 ---> 432
1 // 10 ---> 0 ---> 1
total = total * 10 + 1 ---> 4321 

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

num = int(input('请输入一个正整数：'))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
