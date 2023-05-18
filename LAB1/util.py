"""
 @description: 工具函数
 @author: Harrison-1eo
 @date: 2023/5/18
 @version: 1.0
"""

"""
扩展欧几里得算法
>>>exgcd(2,3)
(-1,1,1)
"""


def exgcd(a, b):
    r, s, t = a, 1, 0
    r_, s_, t_ = b, 0, 1
    while r_ != 0:
        q = r // r_
        temp1 = r - q * r_
        temp2 = s - q * s_
        temp3 = t - q * t_
        r, s, t = r_, s_, t_
        r_, s_, t_ = temp1, temp2, temp3
    ppx, ppy, gcd = s, t, r
    assert gcd > 0
    assert ppx * a + ppy * b == gcd
    return ppx, ppy, gcd


"""
求逆元
>>>inverse(7,mod 5)
3
"""


def inverse(a, m):
    x, _, if1 = exgcd(a, m)
    if if1 != 1:
        print("have no inverse")
        return False
    while x < 0:
        x += m
    return x % m


"""
快速模幂算法 (n>0)
>>>quickMutli(28,668,58)
30
"""


def quickMutli(a, m, n):
    ans = 1
    if m < 0:
        a = inverse(a, n)
        m = (-1) * m
    binary = str(bin(m))[2:]
    for i in binary:
        ans = ans ** 2
        ans = ans * (a ** (int(i)))
        ans = ans % n

    return ans