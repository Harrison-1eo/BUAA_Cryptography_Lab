"""
 @description: RSA 小指数攻击
 @author: Harrison-1eo
 @date: 2023-04-15
 @version: 1.0
"""

TIMES = 1000
import random
from RSAutils import CRT
from gmpy2 import iroot

def _n_random_int(n, num):
    """
    生成num个不同的随机数，范围在[0, n)
    """
    res = []
    for i in range(num):
        r = random.randint(0, n-1)
        if r in res:
            continue
        res.append(r)
    return res

def _input_msg():
    num = int(input())
    e   = int(input())
    c   = []
    N   = []
    for i in range(num):
        c.append(int(input()))
        N.append(int(input()))
    return num, e, c, N

def low_e_attack():
    num, e, c, N = _input_msg()
    msg = []
    for i in range(TIMES):
        r = _n_random_int(num, e)
        # print(r)
        a = [c[j] for j in r]
        m = [N[j] for j in r]
        ans = CRT(a, m)
        p = iroot(ans, e)
        if p[1]:
            if p[0] in msg:
                continue
            msg.append(p[0])
    return msg

if __name__ == '__main__':
    msg = low_e_attack()
    for i in msg:
        print(i)