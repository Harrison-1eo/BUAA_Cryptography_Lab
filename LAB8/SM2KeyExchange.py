"""
 @description: SM2密钥交换算法实现
 @author: Harrison-1eo
 @date: 2023-05-02
 @version: 1.0
"""

from ECCCurve import ECC_curve
from math import ceil, log2
import hashlib


class SM2_key_exchange_util:
    def __init__(self, a, b, p, G, n, hash='sha256'):
        self.curve = ECC_curve(a, b, p)
        self.a = a
        self.b = b
        self.p = p

        if not self.curve.is_on_curve(G):
            raise ValueError("G is not on the curve")
        self.G = G
        self.n = n  # n是G的阶

        self.hash = hash

        self.private_key = None
        self.public_key = None
        self.identity = None
        self.shared_key = None

    def _kdf(self, Z: bytes, klen: int):
        """
        @ param klen: 期望的密钥长度, 单位: 字节
        """
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

    def gen_private_key(self, d=None):
        if d == None:
            d = self.curve.gen_random_number()
        if d < 0:
            raise ValueError("d should be positive")

        self.private_key = d

    def gen_public_key(self, p=None):
        if self.private_key == None:
            raise ValueError("private key is not set")
        if p == None:
            self.public_key = self.curve.multi(self.G, self.private_key)
        else:
            self.public_key = p

    def gen_idenity(self, ID: str):
        self.identity = ID

    def gen_user_information(self, ID: str, P: tuple):
        entlen = len(ID) * 4
        entlen = int.to_bytes(entlen, 2, 'big')

        tmp = entlen + self.curve.int_to_bytes(int(ID, 16)) + self.curve.int_to_bytes(self.a) \
              + self.curve.int_to_bytes(self.b) + self.curve.int_to_bytes(self.G[0]) + self.curve.int_to_bytes(
            self.G[1]) \
              + self.curve.int_to_bytes(P[0]) + self.curve.int_to_bytes(P[1])

        return self._hash(tmp)


class SM2_key_exchange_userA(SM2_key_exchange_util):
    def __init__(self, a, b, p, G, n, hash='sha256'):
        super().__init__(a, b, p, G, n, hash)

        self.user = 'A'

    def gen_shared_key(self, klen=128, ra=None, **kwargs: dict):
        """
        kwarg.keys() = ['Zb', 'Pb', 'Rb', 'Sb']
        """
        if self.private_key == None:
            raise ValueError("private key is not set")
        if self.public_key == None:
            raise ValueError("public key is not set")
        if self.identity == None:
            raise ValueError("identity is not set")
        if 'Zb' not in kwargs.keys():
            raise ValueError("identity of B is not set")
        if 'Pb' not in kwargs.keys():
            raise ValueError("public key of B is not set")
        da = self.private_key
        Pa = self.public_key
        Za = self.identity
        Zb = kwargs['Zb']
        Pb = kwargs['Pb']

        if ra == None:
            ra = self.curve.gen_random_number()

        RA = self.curve.multi(self.G, ra)
        # print(1, RA, sep='\n')
        # yield 1, RA

        x1, y1 = RA[0], RA[1]
        w = ceil((ceil(log2(self.n)) / 2)) - 1
        x1_ = 2 ** w + (x1 & (2 ** w - 1))
        ta = (self.private_key + x1_ * ra) % self.n
        # print(2, ta, sep='\n')
        # yield 2, None

        if 'Rb' not in kwargs.keys():
            raise ValueError("Rb is not set")
        Rb = kwargs['Rb']
        if not self.curve.is_on_curve(Rb):
            raise ValueError("Rb is not on the curve")
        x2, y2 = Rb[0], Rb[1]
        x2_ = 2 ** w + (x2 & (2 ** w - 1))
        tmp = self.curve.multi(Rb, x2_)
        tmp = self.curve.add(Pb, tmp)
        U = self.curve.multi(tmp, ta)
        if U[0] == 0 and U[1] == 0:
            raise ValueError("U is zero")
        # print(3, U, sep='\n')
        # yield 3, None

        # 注意这里的类型转换，需要转换成bytes
        Za_bytes = self.gen_user_information(Za, Pa)
        Zb_bytes = self.gen_user_information(Zb, Pb)
        U0_bytes = self.curve.int_to_bytes(U[0])
        U1_bytes = self.curve.int_to_bytes(U[1])
        msg = U0_bytes + U1_bytes + Za_bytes + Zb_bytes
        Ka_bytes = self._kdf(msg, klen // 8)
        tmp = self._hash(U0_bytes + Za_bytes + Zb_bytes + self.curve.int_to_bytes(x1) + self.curve.int_to_bytes(
            y1) + self.curve.int_to_bytes(x2) + self.curve.int_to_bytes(y2))
        S1 = self._hash(b'\x02' + U1_bytes + tmp)
        # print(4, int.from_bytes(S1, 'big'), sep='\n')
        # yield 4, S1

        Sa = self._hash(b'\x03' + U1_bytes + tmp)
        self.shared_key = int.from_bytes(Ka_bytes, 'big')
        # print(5, int.from_bytes(Sa, 'big'), sep='\n')
        # print('shared key:', self.shared_key)
        # yield 5, Sa
        return self.shared_key, int.from_bytes(S1, 'big'), int.from_bytes(Sa, 'big')


class SM2_key_exchange_userB(SM2_key_exchange_util):
    def __init__(self, a, b, p, G, n, hash='sha256'):
        super().__init__(a, b, p, G, n, hash)

        self.identity = 'B'

        self.db = self.private_key
        self.Pb = self.public_key
        self.Zb = self.gen_idenity(self.identity)

    def gen_shared_key(self, klen=128, rb=None, **kwargs: dict):
        """
        kwarg.keys() = ['Za', 'Pa', 'Ra', 'Sa']
        """
        if self.private_key == None:
            raise ValueError("private key is not set")
        if self.public_key == None:
            raise ValueError("public key is not set")
        if self.identity == None:
            raise ValueError("identity is not set")
        if 'Za' not in kwargs.keys():
            raise ValueError("identity of A is not set")
        if 'Pa' not in kwargs.keys():
            raise ValueError("public key of A is not set")
        db = self.private_key
        Pb = self.public_key
        Zb = self.identity
        Za = kwargs['Za']
        Pa = kwargs['Pa']

        if rb == None:
            rb = self.curve.gen_random_number()

        RB = self.curve.multi(self.G, rb)
        x2, y2 = RB[0], RB[1]
        w = ceil((ceil(log2(self.n)) / 2)) - 1
        x2_ = 2 ** w + (x2 & (2 ** w - 1))
        tb = (self.private_key + x2_ * rb) % self.n
        # yield 1, None

        if 'Ra' not in kwargs.keys():
            raise ValueError("Ra is not set")
        Ra = kwargs['Ra']
        if not self.curve.is_on_curve(Ra):
            raise ValueError("Ra is not on the curve")
        x1, y1 = Ra[0], Ra[1]
        x1_ = 2 ** w + (x1 & (2 ** w - 1))
        tmp = self.curve.multi(Ra, x1_)
        tmp = self.curve.add(Pa, tmp)
        V = self.curve.multi(tmp, tb)
        if V[0] == 0 and V[1] == 0:
            raise ValueError("U is zero")
        # yield 2, None

        # 注意这里的类型转换，需要转换成bytes
        Zb_bytes = self.gen_user_information(Zb, Pb)
        Za_bytes = self.gen_user_information(Za, Pa)
        V0_bytes = self.curve.int_to_bytes(V[0])
        V1_bytes = self.curve.int_to_bytes(V[1])
        msg = V0_bytes + V1_bytes + Za_bytes + Zb_bytes
        Kb_bytes = self._kdf(msg, klen // 8)
        tmp = self._hash(V0_bytes + Za_bytes + Zb_bytes + self.curve.int_to_bytes(x1) + self.curve.int_to_bytes(
            y1) + self.curve.int_to_bytes(x2) + self.curve.int_to_bytes(y2))
        Sb = self._hash(b'\x02' + V1_bytes + tmp)

        S2 = self._hash(b'\x03' + V1_bytes + tmp)

        # if 'Sa' not in kwargs.keys():
        #     raise ValueError("Sa is not set")
        # if S2 != kwargs['Sa']:
        #     raise ValueError("S2 != Sa")
        # yield 4, None

        self.shared_key = int.from_bytes(Kb_bytes, 'big')
        # yield 5, None
        return self.shared_key, int.from_bytes(Sb, 'big'), int.from_bytes(S2, 'big')


if __name__ == '__main__':
    user = input().strip()
    p = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    G = tuple(map(int, input().split()))
    n = int(input().strip())
    IDa = input().strip()
    IDb = input().strip()
    d = int(input().strip())
    Pa = tuple(map(int, input().split()))
    Pb = tuple(map(int, input().split()))
    r = int(input().strip())
    R = tuple(map(int, input().split()))

    if user == 'A':
        sm2 = SM2_key_exchange_userA(a, b, p, G, n)
        sm2.gen_private_key(d)
        sm2.gen_public_key(Pa)
        sm2.gen_idenity(IDa)
        key, S1, Sa = sm2.gen_shared_key(ra=r, Rb=R, Zb=IDb, Pb=Pb)

        print(sm2.shared_key)
        print(S1, Sa)
    elif user == 'B':
        sm2 = SM2_key_exchange_userB(a, b, p, G, n)
        sm2.gen_private_key(d)
        sm2.gen_public_key(Pb)
        sm2.gen_idenity(IDb)
        key, Sb, S2 = sm2.gen_shared_key(rb=r, Ra=R, Za=IDa, Pa=Pa)

        print(sm2.shared_key)
        print(Sb, S2)
