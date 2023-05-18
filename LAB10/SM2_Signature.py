"""
 @description: SM2 数字签名方案。哈希函数采用 SM3
 @author: Harrison-1eo
 @date: 2023/5/18
 @version: 1.0
"""
from LAB9.SM3 import SM3
from LAB8.ECCCurve import ECC_curve
from LAB1.util import inverse

class SM2_signature:
    def __init__(self, a: int, b: int, p: int, G: tuple, n: int):
        self.curve = ECC_curve(a, b, p)
        self.a = a
        self.b = b
        self.p = p
        if not self.curve.is_on_curve(G):
            raise ValueError("G is not on curve")
        self.G = G
        self.n = n

        self.private_key: int = None
        self.public_key: list[int] = None
        self.ID: str = None

    def _hash(self, msg: bytes) -> bytes:
        sm3 = SM3()
        h = sm3.sm3(msg)
        return bytes.fromhex(h)

    def gen_user_information(self) -> bytes:
        """
        生成用户信息: Z_A = H(entlen||ID||a||b||Gx||Gy||Px||Py)
        :return: 用户信息的杂凑值
        """
        P = self.public_key

        entlen = len(self.ID) * 8
        entlen = int.to_bytes(entlen, 2, 'big')

        tmp = entlen + self.ID \
                     + self.curve.int_to_bytes(self.a) + self.curve.int_to_bytes(self.b) \
                     + self.curve.int_to_bytes(self.G[0]) + self.curve.int_to_bytes(self.G[1]) \
                     + self.curve.int_to_bytes(P[0]) + self.curve.int_to_bytes(P[1])

        return self._hash(tmp)

    def sign(self, msg: bytes, k: int) -> tuple:
        """
        生成签名
        :param msg: 待签名消息
        :param k: 随机数
        :return: 签名值
        """
        Za = self.gen_user_information()

        M_ = Za + msg
        e = int.from_bytes(self._hash(M_), 'big')

        x1, y1 = self.curve.multi(self.G, k)

        r = (e + x1) % self.n
        if r == 0 or r + k == self.n:
            raise ValueError("sign failed, retry")

        s = (inverse(1 + self.private_key, self.n) * (k - r * self.private_key)) % self.n
        if s == 0:
            raise ValueError("sign failed, retry")

        return r, s

    def verify(self, msg: bytes, r: int, s: int) -> bool:
        """
        验证签名
        :param msg: 待验证消息
        :param r: 签名值
        :param s: 签名值
        :return: 验证结果
        """

        if r < 1 or r > self.n - 1:
            return False
        if s < 1 or s > self.n - 1:
            return False

        Za = self.gen_user_information()
        M_ = Za + msg
        e = int.from_bytes(self._hash(M_), 'big')

        t = (r + s) % self.n
        if t == 0:
            return False

        p1 = self.curve.multi(self.G, s)
        p2 = self.curve.multi(self.public_key, t)

        x, y = self.curve.add(p1, p2)

        R = (e + x) % self.n

        return R == r


if __name__ == '__main__':
    p = int(input())
    a = int(input())
    b = int(input())
    G = tuple(map(int, input().split()))
    n = int(input())

    sm2 = SM2_signature(a, b, p, G, n)

    ID = input().encode('utf-8')
    Pa = tuple(map(int, input().split()))

    sm2.ID = ID
    sm2.public_key = Pa

    M = input().encode('utf-8')
    mode = input().lower()
    if mode == 'sign':
        da = int(input())
        sm2.private_key = da
        
        k = int(input())
        r, s = sm2.sign(M, k)
        print(r, s, sep='\n')

    elif mode == 'vrfy':
        r = int(input())
        s = int(input())
        print(sm2.verify(M, r, s))
