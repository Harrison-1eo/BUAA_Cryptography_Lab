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
def inverse(a, m):
    x ,_ ,if1 = exgcd(a,m)
    if if1 != 1:
        print("have no inverse")
        return False
    while x < 0:
        x += m
    return x % m

def adjugate_matrix(A):
    n = len(A)
    adj = [[0]*n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            temp = []
            for p in range(n):
                if p == i:
                    continue
                row = []
                for q in range(n):
                    if q == j:
                        continue
                    row.append(A[p][q])
                temp.append(row)
            adj[j][i] = (-1)**(i+j) * determinant(temp)
    
    return adj

def determinant(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    
    det = 0
    for j in range(n):
        temp = []
        for i in range(1,n):
            row = []
            for k in range(n):
                if k == j:
                    continue
                row.append(A[i][k])
            temp.append(row)
        det += (-1)**j * A[0][j] * determinant(temp)
    
    return det

def inverse_matrix(A):
    n = len(A)
    det_A = determinant(A)
    if det_A == 0:
        return None
    
    adj_A = adjugate_matrix(A)
    # inv_A = [[adj_A[i][j]/det_A for j in range(n)] for i in range(n)]
    print(adj_A, det_A)
    return adj_A, det_A

# 矩阵大小n、一个1n的矩阵a和一个nn的矩阵b
def multiply_matrix(n, a, b):
    # 初始化结果矩阵
    result = [0] * n

    # 矩阵乘法计算
    for i in range(n):
        for j in range(n):
            result[i] += a[j] * b[j][i]

    # 返回结果
    return result

def input_value():
    n = int(input())
    d = [[0] * n for _ in range(n)]
    for i in range(n):
        l = input().split(' ')
        for j in range(n):
            d[i][j] = int(l[j])
    return n, d

def slice_matrix(n, msg):
    num = len(msg) // n
    d = [[0] * n for _ in range(num)]
    for i in range(num):
        for j in range(n):
            d[i][j] = ord(msg[i * n + j]) - ord('a')
    return d

def encrypt(n, d, msg):
    ans = ''
    m = slice_matrix(n ,msg)
    for piece in m:
        a = multiply_matrix(n, piece, d)
        for i in a:
            ans += chr((i % 26) + ord('a'))
    return ans

def decrypt(n, d, msg):
    adj_D, det_D = inverse_matrix(d)
    det_D = inverse(det_D, 26)
    ans = ''
    m = slice_matrix(n ,msg)
    for piece in m:
        a = multiply_matrix(n, piece, adj_D)
        for i in a:
            ans += chr((i * det_D % 26) + ord('a'))
    return ans


n, d = input_value()
msg = input().strip()
op = int(input())
if op == 1:
    ans = encrypt(n, d, msg)
elif op == 0:
    ans = decrypt(n, d, msg)
print(ans)
