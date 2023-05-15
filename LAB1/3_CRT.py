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
    if r < 0:
        ppx, ppy, gcd = -ppx, -ppy, -gcd
    assert ppx * a + ppy * b == gcd
    # print(ppx ,a, ppy, b, gcd)
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
中国剩余定理
"""
def cal_Mi(j, m):
    n = len(m)
    Mi = 1
    for i in range(n):
        if i != j:
            Mi *= m[i]
        else:
            continue
    return Mi
def CRT(a,m):
    if len(a) != len(m):
        exit
    n = len(a)
    ans = 0
    multi_m = 1
    for i in range(n):
        multi_m *= m[i]
    for i in range(n):
        Mi = cal_Mi(i, m)
        Ai = a[i]
        ans += Ai * Mi * inverse(Mi,m[i])
        # print(i, Ai , Mi , inverse(Mi,m[i]))
    ans = ans % multi_m
    # 注意题目要求正整数
    while ans <= 0:
        ans += multi_m
    return ans


m = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))

ans = CRT(a, m)
print(ans)