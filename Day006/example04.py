'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-07-04 12:23:29
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-04 16:44:12
FilePath: \Python_learning_Core_code\Day006\example04.py
Description: 显示所有的汉字

~ 汉字的编码范围: 0x4e00 ~ 0x9fa5

~ ord()函数 ---> 查看字符对应的编码
~ chr()函数 ---> 将编码处理成对应的字符

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

print(hex(ord('骆')), hex(ord('昊')))
print(chr(0x9a86), chr(0x660a))
# for i in range(0x4e00, 0x9fa6):
#     print(chr(i), end='')