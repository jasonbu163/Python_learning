# 输入M和N计算C(M,N)
""" 
# 无函数写法
m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fm_n = 1
for num in range(1, m - n + 1):
    fm_n *= num
print(fm // fn // fm_n)

# 函数写法
def fac(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

m = int(input('m = '))
n = int(input('n = '))
print(fac(m) // fac(n) // fac(m - n))
 """

#  函数的参数
""" 
from random import randint

def roll_dice(n = 2):
    # 摇色子
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

def add(a = 0, b = 0, c = 0):
    # 三个数相加
    return a + b + c

# 如果没有指定参数，那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c = 50, a = 100, b = 200))
 """

# 在参数名前面的*表示args是一个可变参数
""" 
def add(*args):
    total = 0
    for val in args:
        total += val
    return total
# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
 """


#  用模块管理函数
""" 
def foo():
    print('hello, world!')

def foo():
    print('goodbye, world!')

# 下面的代码会输出什么呢？
foo()
 """


#  测试不同模块中的foo函数
""" 
from module1 import foo
# 输出hello, world!
foo()
from module2 import foo
# 输出goodbye, world!
foo()

# 也可以这样使用
import module1 as m1
import module2 as m2
m1.foo()
m2.foo()

# 但是如果代码如下的话，程序中调用最后的那个foo，应为后导入的foo覆盖了之前的foo

# 例1
from module1 import foo
from module2 import foo
# 输出goodbye, world!
foo()

# 例2
from module2 import foo
from module1 import foo
# 输出hello, world!
foo()
 """


# 导入module3时，不会执行模块中if条件成立时的代码
# 因为模块的名字时module3而不是__main__
""" import module3 """


# 变量的作用域
""" 
def foo():
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined

if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()
 """


# 说了那么多，其实结论很简单，从现在开始我们可以将Python代码
# 按照下面的格式进行书写，这一点点的改进其实就是在我们理解了
# 函数和作用域的基础上跨出的巨大的一步。

def main():
    # Todo: Add your code here
    pass

if __name__ == '__main__':
    main()