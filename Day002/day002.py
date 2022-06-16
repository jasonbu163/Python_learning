# 使用变量保存数据并进行加减乘除运算
""" 
a = 321
b = 12
print(a + b) #333
print(a - b) #309
print(a * b) #3852
print(a / b) #26.75 
"""

# 使用type()检查变量的类型
""" 
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a)) #<class 'int'>
print(type(b)) #<class 'float'>
print(type(c)) #<class 'complex'>
print(type(d)) #<class 'str'>
print(type(e)) #<class 'bool'>
 """

# 使用input()函数获取键盘输入(字符串)
# 使用int()函数将输入的字符串转换成整数
# 使用print()函数输出带占位符的字符串
""" 
a = int(input('a = '))
b = int(input('b = '))

print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
 """
# **	幂 - 返回x的y次幂	a**b 为10的20次方， 输出结果 100000000000000000000
# //	取整除 - 返回商的整数部分（向下取整），如： 9//2 = 4， -9//2 = -5

# 赋值运算符和符合赋值运算符
""" 
a = 10
b = 3
a += b      #相当于：a = a + b
a *= a + 2  #相当于：a = a * (a + 2)
print(a)
 """

# 比较运算符和逻辑运算符的使用
""" 
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)
print('flag1 =', flag1)
print('flag2 =', flag2)
print('flag3 =', flag3)
print('flag4 =', flag4)
print('flag5 =', flag5)
 """