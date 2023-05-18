"""
 @project: ElGamal.py
 @description: 实现 ElGamal 数字签名方案。哈希函数采用 SHA-256
 @author: Harrison-1eo
 @date: 2023-05-18
 @version: 1.0
"""
from hashlib import sha256
from LAB1.util import inverse


class ElGamal:
    def __init__(self, x, y, p, g) -> None:
        """
        满足 y = g^x mod p
        :param x: 私钥
        :param y: 公钥
        :param p: 素数
        :param g: 生成元
        """
        self.x = x
        self.y = y
        self.p = p
        self.g = g
        
    def _hash(self, m: bytes) -> int:
        return int(sha256(m).hexdigest(), 16)
        
    def sign(self, m: bytes, k: int) -> tuple:
        """
        签名
        :param m: 签名消息
        :param k: 随机数
        :return: 签名
        """
        
        m = self._hash(m)
        r = pow(self.g, k, self.p)
        s = (m - self.x * r) * inverse(k, self.p - 1) % (self.p - 1)
        return r, s
    
    def verify(self, m: bytes, r: int, s: int) -> bool:
        """
        验证签名
        :param m: 签名消息
        :param r: 签名
        :param s: 签名
        :return: 是否验证成功
        """
        
        m = self._hash(m)
        v1 = pow(self.g, m, self.p)
        v2 = (pow(self.y, r, self.p) * pow(r, s, self.p)) % self.p
        return v1 == v2
    

if __name__ == '__main__':
    p = int(input())
    g = int(input())
    m = input().encode('utf-8')
    mode = input().strip()
    if mode.lower() == 'sign':
        x = int(input())
        k = int(input())
        elgamal = ElGamal(x, None, p, g)
        r, s = elgamal.sign(m, k)
        print(r, s)
        
    elif mode.lower() == 'vrfy':
        y = int(input())
        r, s = map(int, input().split())
        elgamal = ElGamal(None, y, p, g)
        print(elgamal.verify(m, r, s))
        