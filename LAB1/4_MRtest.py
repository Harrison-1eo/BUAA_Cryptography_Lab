"""
扩展欧几里得算法
>>>exgcd(2,3)
(-1,1,1)
"""
def exgcd(a, b):
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

"""
求逆元
>>>inverse(7,mod 5)
3
"""
def inverse(a,m):
    x ,_ ,if1 = exgcd(a,m)
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
def quickMutli(a,m,n):
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


"""
Miller-Rabin素性检验
"""
def MRtest(n, test_time = 10):       # test_time 为测试次数,建议设为不小于 8
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

i = int(input())
if MRtest(i) :
    print("YES")
else:
    print("NO")