'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-17 16:45:09
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-17 16:57:12
FilePath: \Python_learning_Core_code\Day002\example07.py
Description: 浮点数的坑

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

print(0.1 + 0.2)
#  ==>  0.30000000000000004
print(0.1 + 0.2 + 0.3)
#  ==>  0.6000000000000001
print(0.3 + 0.2 + 0.1)
#  ==>  0.6

# 所有编程语言都有这个问题
# 如果是做金融行业，用整数运算，算完在给客户输出小数

# 解决这个问题只能用格式化控制
a1 = float(input('a1 = '))
b2 = float(input('b2 = '))

print('%.2f + %.2f = %.1f' % (a1, b2, a1 + b2))
# f - format - 格式化字符串
print(f'{a1} + {b2} = {a1 + b2}')
print(f'{a1:.2f} + {b2:.2f} = {a1 + b2:.1f}') # 和 print('%.2f + %.2f = %.1f' % (a1, b2, a1 + b2)) 效果相同
