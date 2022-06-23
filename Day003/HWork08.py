'''
Author: jasonbu163 jasonbu163@163.com
Date: 2022-06-23 22:21:05
LastEditors: jasonbu163 jasonbu163@163.com
LastEditTime: 2022-06-23 22:33:23
FilePath: \Python_learning_Core_code\Day003\HWork08.py
Description: 找出1-10000以内的完美数(除自身以外所有因子的和等于这个数)
~  6 = 1 + 2 + 3
~  28 = 1 + 2 + 4 + 7 + 14

Copyright (c) 2022 by jasonbu163 jasonbu163@163.com, All Rights Reserved. 
'''
import time


start = time.time()

for num in range(2,10000):
    
    total = 1

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            total += i
            # 防止 49 = 7 * 7 两个因子的情况
            if i != num // i:
                total += num // i

    if total == num:
        print(num)

end = time.time()
print(f'执行时间：{end - start:.3f}秒')