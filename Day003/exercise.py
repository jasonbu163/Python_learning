#  英制单位英寸和公制单位厘米互换
""" 
value = float(input('请输入长度：'))
unit = input('请输入单位：')

if unit == 'in' or unit == '英尺':
    print('%f英尺 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英尺' % (value, value / 2.54))
else:
    print('请输入有效的单位')
 """

#  百分制成绩转换为等级制成绩
""" 
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
 """

#  判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print('三角形的周长：%f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('三角形的面积：%f' % (area))
else:
    print('输入的a,b,c不能构成三角形！！！')