# 生成斐波那契数列的前20个数
""" 
# 我的答案
f1, f2 = 1, 1
print(f1)
print(f2)
for _ in range(18):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f3)

# 大佬的答案
a = 0
b = 1
for _ in range(20):
    a, b = b, a+b
    print(a, end=' ')
print()
 """


# 找出10000以内的完美数
""" 
import math

for num in range(2,10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num //factor != factor:
                result += num //factor
    if result == num:
        print(num)
 """




