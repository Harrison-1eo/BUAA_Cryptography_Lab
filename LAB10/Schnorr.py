"""
 @project: Schnorr.py
 @description: 实现 Schnorr 数字签名方案。哈希函数采用 SHA-1
 @author: Harrison-1eo
 @date: 2023-05-16
 @version: 1.0
"""

import random
import hashlib


class Schnorr:
    def __init__(self, p, q, g):
        self.p = p
        self.q = q
        self.g = g
        
    def sign(self, x: int, m: str, k: int = None):
        """
        discription: 签名函数
        :param x: 私钥
        :param m: 消息
        :param k: 随机数
        :return: 签名
        """
        if k is None:
            k = random.randint(1, self.q - 1)
        r = pow(self.g, k, self.p)
        
        m = (m + str(r)).encode('utf-8')
        e = int(hashlib.sha1(m).hexdigest(), 16)
        
        s = (k + x * e) % self.q
        
        return (e, s)
    
    def verify(self, y: int, m: str, r: tuple):
        """
        discription: 验证函数
        :param y: 公钥
        :param m: 消息
        :param r: 签名
        """
        e, s = r
        r_ = pow(self.g, s, self.p) * pow(y, e, self.p) % self.p
        
        m = (m + str(r_)).encode('utf-8')
        e_ = int.from_bytes(hashlib.sha1(m).digest(), byteorder='big')
        
        return e == e_
    

if __name__ == '__main__':
    p = int(input())
    q = int(input())
    g = int(input())
    
    sch = Schnorr(p, q, g)
    
    msg = input()
    mode = input().strip()
    if mode.lower() == 'sign':
        x = int(input())
        k = int(input())
        ans = sch.sign(x, msg, k)
        print(ans[0], ans[1])
        
    elif mode.lower() == 'vrfy':
        y = int(input())
        r = [int(i) for i in input().split()]
        ans = sch.verify(y, msg, r)
        print(ans)
        
    
        
        
        
    
        