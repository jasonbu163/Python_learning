'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-17 15:47:11
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-17 16:19:37
FilePath: \Python_learning_Core_code\Day002\example06.py
Description: 整数的表示法

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

# 十进制
a = 110
# 八进制
b = 0o110
# 十六进制
c = 0x110
# 二进制
d = 0b110
# 浮点数的科学计数法
e = 123e-5
print(a, b, c, d, e)

# bin ---> binary ---> 十进制转二进制
print(bin(47))
# oct ---> octal ---> 十进制转八进制
print(oct(47))
# hex ---> hexadecimal ---> 十进制转十六进制
print(hex(47))