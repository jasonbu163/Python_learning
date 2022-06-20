'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-17 16:02:23
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-20 18:07:04
FilePath: \Python_learning_Core_code\Day003\example01.py
Description: 分支结构（选择结构）的例子

~ 用户身份验证
~ 代码中有多条执行路径，但是只有其中一条会被执行

admin / Admin123!!

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''
import getpass

username = input('请输入用户名：')
password = getpass.getpass('请输入密码： ')

if username == 'admin' and password == 'Admin123!!':
    print('-------------------------')
    print('身份验证成功！')
    print('欢迎使用XXX系统！')
    print('客服热线：400-800-8800')
else:
    print('-------------------------')
    print('身份验证失败！')
    print('用户名或密码错误！')
print('-------------------------')
print('程序结束，再见！')