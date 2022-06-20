'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-17 16:33:56
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-17 16:35:00
FilePath: \Python_learning_Core_code\Day003\exercise02.py
Description: 百分制成绩转换为等级制成绩

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''

score = float(input('请输入成绩：'))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是：',grade)