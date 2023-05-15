"""
 @description: RSA 算法的工具函数，包括生成随机素数、生成随机整数、求逆元、快速模幂、中国剩余定理、扩展欧几里得算法、求最大公因子等。
 @author: Harrison-1eo
 @date: 2023-04-15
 @version: 1.0
"""


def s2n(s: str):
    if isinstance(s, str):
        s = s.encode("utf-8")
    return int.from_bytes(s, "big")


def n2s(n: int):
    if not isinstance(n, int):
        raise TypeError("len_in_bits defined only for ints")
    nbits = n.bit_length()
    nbytes = (nbits + 7) >> 3
    return n.to_bytes(nbytes, "big")


def gcd(a, b):
    """
    求最大公因子，使用辗转相除法
    """
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def exgcd(a, b):
    """
    扩展欧几里得算法
    >>>exgcd(2,3)
    (-1,1,1)
    """
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


def inverse(a, m):
    """
    求逆元
    inverse(7,mod 5)
    3
    """
    x, _, if1 = exgcd(a, m)
    if if1 != 1:
        print("have no inverse")
        return False
    while x < 0:
        x += m
    return x % m


def quick_mutli(a, m, n):
    """
    快速模幂算法 (n>0)
    quickMutli(28,668,58) 计算 28^668 mod 58
    30
    """
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


def cal_Mi(a, m):
    n = len(m)
    Mi = 1
    for i in range(n):
        if i != a:
            Mi *= m[i]
        else:
            continue
    return Mi


def CRT(a, m):
    """
    中国剩余定理
    """
    if len(a) != len(m):
        print('error 1')
        exit()
    n = len(a)
    ans = 0
    multi_m = 1
    for i in range(n):
        multi_m *= m[i]
    for i in range(n):
        Mi = cal_Mi(i, m)
        Ai = a[i]
        ans += Ai * Mi * inverse(Mi, m[i])
    ans = ans % multi_m
    return ans


def fermat_test(n, rounds=10):
    """
    费马检验
    rounds: 测试次数，建议不小于 10
    """
    import random
    for i in range(rounds):
        b = int((n - 4) * random.random() + 2)  # 生成一个[2,n-2]之间的随机整数
        if gcd(b, n) > 1:
            return False
        r = quick_mutli(b, n - 1, n)
        if r != 1:
            return False
    return True


def MR_test(n, test_time=10):
    """
    Miller-Rabin素性检验
    test_time: 测试次数，建议不小于 8
    """
    from random import randint
    if n < 3:
        return n == 2
    u = n - 1  # 将n-1 = u*(2^t)， 计算出u跟t
    t = 0
    while u % 2 == 0:
        u //= 2
        t += 1
    for i in range(1, test_time + 1):  # 用费马小定理测试test_time次
        x = randint(2, n - 1)
        # a ^ (n - 1) = a ^ (u * 2t) = (a ^ u) ^ (2t)
        v = quick_mutli(x, u, n)  # 计算a ^ u % n
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


def make_random_key(n=1024):
    """
    生成两个大素数作为密钥p, q
    """
    p = get_random_Nbit_prime(n)
    q = get_random_Nbit_prime(n)
    while p == q:
        q = get_random_Nbit_prime(n)
    return p, q


def get_random_Nbit_prime(N):
    """
    N位素数生成
    """
    number = get_random_Nbit_integer(N) | 1
    while (not is_prime(number)):
        number = number + 2
    return number


def get_random_Nbit_integer(N):
    """
    N位大数生成
    """
    from random import randint
    return randint(2 ** (N - 1), 2 ** N)


def is_prime(number):
    """
    素性检测
    """
    if fermat_test(number):
        if MR_test(number):
            return True
    return False


def ceil(a):
    """
    向上取整
    """
    if a == int(a):
        return int(a)
    else:
        return int(a) + 1


def RSAdecrypt_CRT(c, d, p, q):
    """
    RSA解密算法，使用中国剩余定理加速，d已经被算出
    """
    a = []
    m = []
    a1 = quick_mutli(c % p, d % (p - 1), p)
    a2 = quick_mutli(c % q, d % (q - 1), q)
    a.append(a1)
    a.append(a2)
    m.append(p)
    m.append(q)
    x = CRT(a, m)
    return x
