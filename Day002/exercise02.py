# 输入元的半径计算周长和面积
# 我的答案

r = float(input('请输入圆的半径：'))
pi = 3.1416
d = pi * r * 2
S = pi * r * r
print(f'圆的周长为：{d:.2f}')
print('圆的面积为：%.2f' % S)

# 老师的答案

radius = float(input('请输入圆的半径：'))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)
