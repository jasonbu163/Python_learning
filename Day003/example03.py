'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-23 11:12:55
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 11:26:40
FilePath: \Python_learning_Core_code\Day003\example03.py
Description: 工资薪金（按月）个人所得税速算表

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

total = float(input('本月收入：'))
insurance = float(input('五险一金扣除：'))

E = total - insurance
I = E - 3500

if 0 < I <= 1500:
    R = 0.03
    D = 0
elif I <= 4500:
    R = 0.1
    D = 105   
elif I <= 9000:
    R = 0.2
    D = 555   
elif I <= 35000:
    R = 0.25
    D = 1005
elif I <= 55000:
    R = 0.3
    D = 2755
elif I <= 80000:
    R = 0.35
    D = 5505
else:
    R = 0.45
    D = 13505

if I > 0:
    T = I * R - D
else:
    T = 0

print(f'应纳税款：{T:.2f}元')
print(f'税后收入；{E - T:.2f}元')
