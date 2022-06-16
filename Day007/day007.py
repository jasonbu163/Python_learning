# 使用字符串

# s1 = 'hello, world!'
# s2 = "hello, world!"
# s3 = """
# hello,
# world!
# """
# print(s1, s2, s3, end='') 
""" 
s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)
 """
# 不希望\表示转义，可以在字符串最前面加上r，如下
""" 
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')
 """

# 通过一系列方法对字符串进行处理
""" 
s1 = 'hello ' * 3
print(s1) # hello hello hello
s2 = 'world'
s1 += s2
print(s1) # hello hello hello world
print('ll' in s1) # True
print('good' in s1) # False
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2]) # c
# 字符串切片(从指定的开始索引到指定的结束索引) 
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246
print(str2[::-1]) # 654321cba
print(str2[-3:-1]) # 45
 """
""" 
str1 = 'hello, world!'
# 通过内置函数len计算字符串长度
print(len(str1)) # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, world!
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or')) # 8
print(str1.find('shit')) # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # True
# 将字符串以指定宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))

str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit()) # False
# 检查字符串是否由字母构成
print(str2.isalpha()) # False
# 检查字符串是否由字母和数字构成
print(str2.isalnum()) # True

str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())
 """

# 格式化输出字符串
# 法一
""" 
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
 """
# 法二
""" 
a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))
 """
# Python 3.6以后格式化字符串的代码表达方式更为简洁
""" 
a, b = 5, 10
print(f'{a} * {b} = {a * b}')
 """


# 使用列表
""" 
list1 = [1, 3, 5, 7, 100]
print(list1) # [1, 3, 5, 7, 100]
# 乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2) # ['hello', 'hello', 'hello']
# 计算列表长度(元素个数)
print(len(list1)) # 5
# 下标(索引)运算
print(list1[0]) # 1
print(list1[4]) # 100
# print(list1[5]) # IndexError: list index out of range
print(list1[-1]) # 100
print(list1[-3]) # 5
list1[2] = 300
print(list1) # [1, 3, 300, 7, 100]
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历列表元素
for elem in list1:
    print(elem, end=' ')
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)
 """


# 向列表中添加元素以及如何从列表中移除元素
""" 
list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)
list1.insert(1, 400)
# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1) # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(len(list1)) # 9
# 先通过成员运算判断元素是否在列表中，如果存在就删除
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1) # [1, 400, 5, 7, 100, 200, 1000, 2000]
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1) # [400, 5, 7, 100, 200, 1000]
# 清空列表元素
list1.clear()
print(list1) # []
 """


# 列表也可以做切片操作
""" 
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
print(fruits)
# 列表切片
fruits2 = fruits[1: 4]
print(fruits2) # ['apple', 'strawberry', 'waxberry']
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3: -1]
print(fruits4) # ['pitaya', 'pear']
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']
 """

#  对列表的排序操作
""" 
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True) # 先按字母顺序排序，在z~a逆转顺序
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print('list1 = ', list1) # ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
print('list2 = ', list2) # ['apple', 'blueberry', 'internationalization', 'orange', 'zoo']
print('list3 = ', list3) # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
print('list4 = ', list4) # ['zoo', 'apple', 'orange', 'blueberry', 'internationalization']
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1) # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
 """


# 生成式和生成器
""" 
import sys
# 使用列表的生成式语法来创建列表
f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f)) # 查看对象占用内存的字节数
print(f)
# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f)) # 相比生成式生成器不占用存储数据的空间
print(f)
for val in f:
    print(val)
 """


# 通过yield关键字将一个普通函数改造成生成器函数
# 斐波拉切数列可以通过下面递归的方法来进行定义
""" 
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

def main():
    for val in fib(20):
        print(val)

if __name__ == '__main__':
    main()
 """


# 使用元组
""" 
# 定义元组
t = ('罗小黑', 38, True, '四川成都')
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])
# 遍历元组中的值
for member in t:
    print(member)
# 重新给元组赋值
# t[0] = '王大锤'  # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('王大锤', 20, True, '云南昆明')
print(t)
# 将元组转换成列表
person = list(t)
print(person)
# 列表是可以修改它的元素的
person[0] = '李小龙'
person[1] = 25
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_list)
print(fruits_tuple)
 """
""" 
如果不需要对元素进行添加、删除、修改的时候，
可以考虑使用元组，当然如果一个方法要返回多个值，
使用元组也是不错的选择。

元组在创建时间和占用的空间上面都优于列表。
 """


#  使用集合
""" 
# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 10) if num % 3 == 0 or num % 5 == 0}
print(set4)

print()
# 向集合添加元素和从集合删除元素。
set1.add(4)
set1.add(5)
print(set1) # {1, 2, 3, 4, 5}
set2.update([11, 12]) 
print(set2) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}
set2.discard(5)
print(set2) # {1, 2, 3, 4, 6, 7, 8, 9, 11, 12}
if 4 in set2:
    set2.remove(4)
print(set2) # {1, 2, 3, 6, 7, 8, 9, 11, 12}
print()
print(set1, set2) # {1, 2, 3, 4, 5} {1, 2, 3, 6, 7, 8, 9, 11, 12}
print(set3.pop()) # 1
print(set3) # {2, 3}


print()
print(set1, set2, set3) # {1, 2, 3, 4, 5} {1, 2, 3, 6, 7, 8, 9, 11, 12} {2, 3}

# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))

# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))
 """


#  使用字典

# 创建字典的字面量语法
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
print(scores)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'],'123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)
# 通过键可以获取字典中对应的值
print(scores['骆昊'])
print(scores['狄仁杰'])
# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')
# 更新字典中的元素
scores['白元芳'] = 65
scores['诸葛王朝'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60))
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('骆昊', 100))
print(scores)
# 清空字典
scores.clear()
print(scores)
