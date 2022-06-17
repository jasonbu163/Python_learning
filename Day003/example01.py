'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-17 16:02:23
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-17 16:31:45
FilePath: \Python_learning_Core_code\Day003\example01.py
Description: 用户身份验证

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

username = input('请输入用户名：')
password = input('请输入密码： ')

if username == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')