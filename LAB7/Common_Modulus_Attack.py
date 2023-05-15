"""
 @description: RSA 共模攻击
 @author: Harrison-1eo
 @date: 2023-04-15
 @version: 1.0
"""
from RSAutils import exgcd, quick_mutli

def _input_msg():
    e1 = int(input())
    e2 = int(input())
    c1 = int(input())
    c2 = int(input())
    N  = int(input())
    return e1, e2, c1, c2, N

def common_modulus_attack():
    e1, e2, c1, c2, N = _input_msg()
    ppx, ppy, _ = exgcd(e1, e2)
    m1 = quick_mutli(c1, ppx, N) % N
    m2 = quick_mutli(c2, ppy, N) % N
    m = (m1 * m2) % N
    return m

if __name__ == '__main__':
    msg = common_modulus_attack()
    print(msg)
