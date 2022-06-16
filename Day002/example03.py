# 使用input()函数获取键盘输入(字符串)
# 使用int()函数将输入的字符串转换成整数
# 使用print()函数输出带占位符的字符串

a = int(input('a = '))
b = int(input('b = '))

print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

# **	幂 - 返回x的y次幂	a**b 为10的20次方， 输出结果 100000000000000000000
# //	取整除 - 返回商的整数部分（向下取整），如： 9//2 = 4， -9//2 = -5