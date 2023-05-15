"""
 @description: RSA 已知e, d, N，分解N = p * q
 @author: Harrison-1eo
 @date: 2023-04-15
 @version: 1.0
"""

# 参考：https://blog.csdn.net/weixin_44110537/article/details/107869682

import random
from gmpy2 import powmod, gcd

def _input_msg():
    e = int(input())
    d = int(input())
    N = int(input())
    return e, d, N

def getpq():
    e, d, n = _input_msg()
    while True:
        k = e * d - 1
        g = random.randint(0, n)
        while k % 2 == 0:
            k = k//2
            temp = powmod(g, k, n) - 1
            if gcd(temp, n) > 1 and temp != 0:
                return gcd(temp, n), n // gcd(temp, n)

if __name__ == '__main__':
    p, q = getpq()
    # 小数先输出
    print(min(p, q))
    print(max(p, q))
