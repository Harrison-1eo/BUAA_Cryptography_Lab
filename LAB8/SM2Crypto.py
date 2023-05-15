"""
 @description: SM2公钥加解密算法实现
 @author: Harrison-1eo
 @date: 2023-04-30
 @version: 1.0
"""


from ECCCurve import ECC_curve
from math import ceil
import hashlib

class SM2_encryptor():
    def __init__(self, a, b, p, G, hash = 'sha256'):
        self.curve = ECC_curve(a, b, p)
        self.a = a
        self.b = b
        self.p = p

        if not self.curve.is_on_curve(G):
            raise ValueError("G is not on the curve")
        self.G = G

        self.hash = hash

    def _kdf(self, Z: bytes, klen: int):
        if self.hash == 'sha256':
            v = 32

        ct = 0x00000001
        Ha = []
        rcnt = ceil(klen / v)

        for i in range(rcnt):
            msg = Z + int.to_bytes(ct, 4, 'big')
            Ha.append(self._hash(msg))
            ct += 1

        Ha = b''.join(Ha)[:klen]

        return Ha

    def _hash(self, msg: bytes):

        return hashlib.sha256(msg).digest()

    def encrypt(self, Pb: tuple, msg: bytes, k) -> bytes:
        klen = len(msg)

        C1 = self.curve.multi(self.G, k)
        x1, y1 = C1
        if x1 == 0 and y1 == 0:
            raise ValueError("C1 is zero")
        x1 = self.curve.int_to_bytes(x1)
        y1 = self.curve.int_to_bytes(y1)
        plen = ceil(self.p.bit_length() / 8)
        x1 = b'\x00' * (plen - len(x1)) + x1
        y1 = b'\x00' * (plen - len(y1)) + y1
        C1 = b'\x04' + x1 + y1

        S  = self.curve.multi(Pb, k)

        x2, y2 = S
        if x2 == 0 and y2 == 0:
            raise ValueError("S is zero")
        x2 = self.curve.int_to_bytes(x2)
        y2 = self.curve.int_to_bytes(y2)

        t = self._kdf(x2 + y2, klen)
        if t == 0:
            raise ValueError("t is zero")

        C2 = bytes([i ^ j for i, j in zip(msg, t)])
        C3 = self._hash(x2 + msg + y2)

        res = C1 + C2 + C3

        return res
    
    def decrypt(self, d: int, C: bytes) -> bytes:
        if C[0] != 0x04:
            raise ValueError("C1 is not a point")
        
        plen = ceil(self.p.bit_length() / 8)
        x1 = C[1:plen + 1]
        y1 = C[plen + 1:plen * 2 + 1]
        C1 = (int.from_bytes(x1, 'big'), int.from_bytes(y1, 'big'))
        C2 = C[plen * 2 + 1:-32]
        C3 = C[-32:]
        klen = len(C2)

        if not self.curve.is_on_curve(C1):
            raise ValueError("C1 is not on the curve")

        S = self.curve.multi(C1, d)
        x2, y2 = S
        if x2 == 0 and y2 == 0:
            raise ValueError("S is zero")
        
        x2 = self.curve.int_to_bytes(x2)
        y2 = self.curve.int_to_bytes(y2)

        t = self._kdf(x2 + y2, klen)
        if t == 0:
            raise ValueError("t is zero")

        msg = bytes([i ^ j for i, j in zip(C2, t)])

        C3_ = self._hash(x2 + msg + y2)
        if C3 != C3_:
            raise ValueError("C3 is not equal to C3_")

        return msg

if __name__ == "__main__":
    p = int(input())
    a = int(input())
    b = int(input())

    G = input().split(' ')
    G = (int(G[0]), int(G[1]))

    sm2 = SM2_encryptor(a, b, p, G)

    Par = input().strip()
    op  = int(input())
    msg = input().strip()
    msg = bytes.fromhex(msg[2:])

    if op == 1:
        pb = input().split(' ')
        pb = (int(pb[0]), int(pb[1]))
        k  = int(input())

        res = sm2.encrypt(pb, msg, k)
        print('0x' + res.hex())

    elif op == 0:
        d = int(input())
        res = sm2.decrypt(d, msg)
        print('0x' + res.hex())

    else:
        raise ValueError("op is not 0 or 1")

    
