"""
 @description: BBS伪随机数发生器
 @author: Harrison-1eo
 @date: 2023-04-12
 @version: 1.0
"""


def exgcd(a, b):
    """
    扩展欧几里得算法
    :param a: int
    :param b: int
    :return: (x, y, gcd(a, b))
    """
    r, s, t = a, 1, 0
    r_, s_, t_ = b, 0, 1
    while r_ != 0:
        q = r//r_
        temp1 = r-q*r_
        temp2 = s-q*s_
        temp3 = t-q*t_
        r, s, t = r_, s_, t_
        r_, s_, t_ = temp1, temp2, temp3
    ppx, ppy, gcd = s, t, r
    assert gcd > 0  
    assert ppx * a + ppy * b == gcd
    return ppx, ppy, gcd

def inverse(a,m):
    """
    求逆元
    :param a: int
    :param m: int
    :return: a ^ (-1) (mod m): int
    """
    x ,_ ,if1 = exgcd(a,m)
    if if1 != 1:
        print("have no inverse")
        return False
    while x < 0:
        x += m
    return x % m

def quickMutli(a,m,n):
    """
    快速模幂算法 (n>0)
    :param a: int
    :param m: int
    :param n: int
    :return: a ^ m (mod n): int
    """
    ans = 1
    if m < 0:
        a = inverse(a,n)
        m = (-1)*m
    binary = str(bin(m))[2:]
    for i in binary:
        ans = ans ** 2
        ans = ans * (a ** (int (i)))
        ans = ans % n
    
    return ans

def MRtest(n: int, test_time = 10):
    """
    Miller-Rabin素性检验
    :param n: int, 待检验的数
    :param test_time: int, 测试次数，建议设为不小于 8
    :return: True or False
    """
    from random import randint
    if n < 3:
        return n == 2
    u = n - 1                           # 将n-1 = u*(2^t)， 计算出u跟t
    t = 0
    while u % 2 == 0:
        u //= 2
        t += 1
    for i in range(1, test_time + 1):   # 用费马小定理测试test_time次
        x = randint(2, n - 1)
        # a ^ (n - 1) = a ^ (u * 2t) = (a ^ u) ^ (2t)
        v = quickMutli(x, u, n) # 计算a ^ u % n
        if v == 1 or v == n - 1:
            continue
        for j in range(t + 1):
            # 验证 x ^ 2 = 1 (mod p) 的解为x = 1 or x = p - 1
            v = v * v % n 
            if v == n - 1:
                break
        else:
            return False
    return True

def getPrime(n):
    """
    生成n位素数
    :param n: int
    :return: int
    """
    from random import randint
    while True:
        num = randint(2**(n-1),2**n)
        if MRtest(num):
            return num
        
def getPrime3mod4(n):
    """
    生成n位素数，且满足p % 4 = 3
    :param n: int
    :return: int
    """
    from random import randint
    while True:
        num = randint(2**(n-1),2**n)
        if MRtest(num) and num % 4 == 3:
            return num

def getPrime3mod4Pair(n):
    """
    生成n长的两个不同素数，且满足p % 4 = 3
    :param n: int
    :return: (p,q)
    """
    while True:
        p = getPrime3mod4(n)
        q = getPrime3mod4(n)
        if p != q:
            return p,q
        
def BBS(p: int, q: int, s: int, length: int):
    """
    BBS算法
    输入：素数p,q，种子s，随机数长度length
    输出：随机数
    """
    N = p * q
    x = s ** 2 % N
    ans = 0
    for i in range(length):
        x = x ** 2 % N
        # ans = ans * 2 + (x & 1)
        ans += ((x & 1) << i)
    return ans

if __name__ == "__main__":
    # p,q = getPrime3mod4Pair(512)
    # r = getPrime(512)
    length = int(input())
    p = int(input())
    q = int(input())
    s = int(input())
    print(BBS(p, q, s, length))
    
