"""
 @description: Wiener's attack, RSA维纳攻击
 @author: Harrison-1eo
 @date: 2023-04-19
 @version: 1.0
"""

import gmpy2

def transform(x, y):  # 使用辗转相处将分数 x/y 转为连分数的形式
    res = []
    while y:
        res.append(x // y)
        x, y = y, x % y
    return res


def continued_fraction(sub_res):
    numerator, denominator = 1, 0
    sub_res = sub_res[::-1]
    for i in sub_res:  # 从sublist的后面往前循环
        denominator, numerator = numerator, i * numerator + denominator
    return denominator, numerator  # 得到渐进分数的分母和分子，并返回


def get_pq(a, b, c):  # 由p+q和pq的值通过维达定理来求解p和q
    par = gmpy2.isqrt(b * b - 4 * a * c)  # 由上述可得，开根号一定是整数，因为有解
    x1, x2 = (-b + par) // (2 * a), (-b - par) // (2 * a)
    return x1, x2


def wienerAttack(e, n):
    fraction = transform(e, n)
    fraction = list(map(continued_fraction, (fraction[0:i] for i in range(1, len(fraction)))))
    # ed = 1 (mod φ(n))
    # ed = 1 + φ(n)
    # e/φ(n) - k/d = 1/(d*φ(n))
    # e/N - k/d = 1/(d*φ(n))
    for (d, k) in fraction:  # 用一个for循环来注意试探e/n的连续函数的渐进分数，直到找到一个满足条件的渐进分数
        if k == 0:   # 可能会出现连分数的第一个为0的情况，排除
            continue
        if (e * d - 1) % k != 0:  # ed=1 (mod φ(n)) 因此如果找到了d的话，(ed-1)会整除φ(n),也就是存在k使得(e*d-1)//k=φ(n)
            continue

        phi = (e * d - 1) // k  # 这个结果就是 φ(n)
        px, qy = get_pq(1, n - phi + 1, n)
        if px * qy == n:
            p, q = abs(int(px)), abs(int(qy))  # 可能会得到两个负数，负负得正未尝不会出现
            d = gmpy2.invert(e, (p - 1) * (q - 1))  # 求ed=1 (mod  φ(n))的结果，也就是e关于 φ(n)的乘法逆元d
            return p, q, d



e = int(input(), 10)
n = int(input(), 10)
ans = wienerAttack(e, n)
for i in ans:
    print(i)