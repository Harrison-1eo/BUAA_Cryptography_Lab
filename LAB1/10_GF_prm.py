# 多项式除法
def GF_div(a, b):
    ans = 0
    while len(bin(a)) >= len(bin(b)):
        rec = len(bin(a)) - len(bin(b))
        a ^= (b << rec)
        ans ^= (1 << rec)
    return ans, a
    #return hex(ans)[2:].rjust(2, '0')+' '+hex(a)[2:].rjust(2, '0')

# 生成n//2次方下所有的不可约多项式
def irreducible(n):
    ans = []
    if n == 1:
        return [0b10, 0b11]
    else:
        # 递归，先算出n-1次不可约，再算n次不可约
        factor = irreducible(n - 1)
        for i in factor:
            ans.append(i)
        right = 2 ** (n + 1)
        left = 2 ** (n)
        # print('range: ', n, bin(left), bin(right))
        for i in range(left, right):
            if tell_irPoly(i, factor):
                # print('append:', bin(i))
                ans.append(i)
    # 返回多项式列表
    return ans

# 遍历，用于判断是否是本原多项式
def tell(n):
    ir = []
    ans = []
    factor = irreducible(n // 2)
    right = 2 ** (n + 1)
    left = 2 ** (n)
    for i in range(left, right):
        # 首先判断是否是不可约多项式，如果是，添加到ir列表里
        if tell_irPoly(i, factor):
            # print('append:', bin(i))
            ir.append(i)
    for i in ir:
        # 然后在不可约多项式列表中判断是否是本原多项式
        if tell_primPoly(i, n):
            ans.append(i)
    return ans

# 不可约多项式判断，输入一个多项式和n//2次方下所有的不可约多项式的列表，返回布尔值
def tell_irPoly(m, factor):
    for j in factor:
        if GF_div(m, j)[1] == 0:
            return False
    return True

# 本原多项式判断，输入多项式和次数n，返回布尔值
def tell_primPoly(fx, n):
    m = 2 ** n - 1
    fm = (1 << m) + 1
    if GF_div(fm, fx)[1] == 0:
        for i in range(1, m):
            fq = (1 << i) + 1
            if GF_div(fq, fx)[1] == 0:
                return False
        return True
    return False

#n = int(input())
n = 2
l = tell(n)
for i in l:
    print(bin(i)[2:], end=' ')