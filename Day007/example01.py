'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-07-07 20:24:16
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-07-07 22:36:36
FilePath: \Python_learning_Core_code\Day007\example01.py
Description: 保存5个学生, 3门课程的成绩

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''
import random


names = ['关羽', '张飞', '赵云', '马超', '黄忠', '典韦', '吕布']
courses = ['语文', '数学', '英语']
scores = [[random.randrange(50, 101) for _ in range(len(courses))] for _ in range(len(names))]
print(scores)
# for i, name in enumerate(names):
#     for j, course in enumerate(courses):
#         print(f'{name}的{course}成绩：{scores[i][j]}')

# 统计每个学生的平均成绩
for i, name in enumerate(names):
    print(f'{name}平均成绩：{sum(scores[i]) / len(courses):.1f}')

# 统计每门课的最高分和最低分
for j, courses in enumerate(courses):
    temp = [scores[i][j] for i in range(len(names))]
    print(f'{courses}的最高分：{max(temp)}')
    print(f'{courses}的最低分：{min(temp)}')
