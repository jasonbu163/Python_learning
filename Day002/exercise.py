# 将华氏温度转换为摄氏温度
""" 
f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c)) 
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
 """


# 输入元的半径计算周长和面积
# 我的答案
""" 
r = float(input('请输入圆的半径：'))
pi = 3.1416
d = pi * r * 2
S = pi * r * r
print(f'圆的周长为：{d:.2f}')
print('圆的面积为：%.2f' % S)
 """
# 大佬的答案
""" 
radius = float(input('请输入圆的半径：'))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)
 """


# 输入年份 如果是闰年输出True 否则输出False

year = int(input('请输入年份：'))
# 如果代码太长写一行不便于阅读 可以使用\对代码进行折行
is_leap = year % 4 == 0 and year % 100 != 0 or \
    year % 400 == 0
print(is_leap)
