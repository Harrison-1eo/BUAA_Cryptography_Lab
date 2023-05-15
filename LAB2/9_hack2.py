from fractions import Fraction
import random

# 扩展欧几里得算法
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

# 求逆元
def inverse(a, m):
    x ,_ ,if1 = exgcd(a,m)
    if if1 != 1:
        print("have no inverse")
        return False
    while x < 0:
        x += m
    return x % m

# 伴随矩阵的计算
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
            adj[j][i] = (-1)**(i+j) * determinant_matrix(temp)
    
    return adj

# 矩阵行列式的计算
def determinant_matrix(A):
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
        det += (-1)**j * A[0][j] * determinant_matrix(temp)
    
    return det

# 逆矩阵的计算，返回值为A的伴随矩阵和A的模26下的行列式
# 不直接返回逆矩阵防止小数计算丢失精度
def inverse_matrix(A):
    n = len(A)
    det_A = determinant_matrix(A)
    if det_A == 0:
        return None
    
    adj_A = adjugate_matrix(A)
    # inv_A = [[adj_A[i][j]/det_A for j in range(n)] for i in range(n)]
    
    return adj_A, det_A % 26

# 两个矩阵的乘法，返回一个矩阵
def multiply_matrix(matrix1,matrix2):
    new_matrix = [[0 for i in range(len(matrix1))] for j in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            for x in range(len(matrix1)):
                new_matrix[i][j] += matrix1[i][x]*matrix2[x][j]   
    return new_matrix

# 对给出的消息和密文按照密钥长度切片，存储值为0-25，返回二维矩阵
def slice_matrix(n, msg):
    num = len(msg) // n
    d = [[0] * n for _ in range(num)]
    for i in range(num):
        for j in range(n):
            d[i][j] = ord(msg[i * n + j]) - ord('a')
    return d

# 判断a是否在l列表中
def list_exist(a, l):
    for i in l:
        if a == i:
            return True
    return False

# 在a到b的闭区间上随机生成num个整数，返回列表
def random_int(a, b, num):
    l = []
    while len(l) < num:
        i = random.randint(a, b)
        if list_exist(i, l) == False:
            l.append(i)
    return l

# 在切片中随机抽出三组数据
def random_matrix(n, msg_M, key_M):
    m_l = random_int(0, len(msg_M) - 1, n)
    msg = []
    key = []
    for i in m_l:
        msg.append(msg_M[i])
        key.append(key_M[i])
    return msg, key

def decrypt(n, msg_M, key_M):
    count = 0
    # 在明文和密文中随机取出n组，如果明文矩阵的行列式与26互素，则满足条件，可以进行解密
    while True:
        count += 1
        msg, key = random_matrix(n, msg_M, key_M)
        adj_msg, det_msg = inverse_matrix(msg)
        flag = exgcd(det_msg, 26)[2]
        if flag == 1:
            break
    
    # 明文矩阵的逆和密文矩阵相乘，所得矩阵为加密矩阵
    tmp = multiply_matrix(adj_msg, key)
    ans = [[Fraction(tmp[i][j], det_msg) for j in range(n)] for i in range(n)]

    return ans, count

n = int(input())
msg = input().strip()
key = input().strip()
msg_M = slice_matrix(n, msg)
key_M = slice_matrix(n, key)
ans, count = decrypt(n, msg_M, key_M)

for i in ans:
    for j in i:
        # 注意运算是定义在有限域上的，除法为求逆操作
        d = inverse(j.denominator, 26) * j.numerator % 26
        print(d, end=' ')
    print()