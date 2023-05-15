"""
 @description: ECDH(Elliptic Curve Diffie-Hellman)椭圆曲线迪菲-赫尔曼密钥交换协议,它是一种基于椭圆曲线密码学的密钥交换协议
 @author: Harrison-1eo
 @date: 2023-04-29
 @version: 1.0
"""

from ECCCurve import ECC_curve

class ECDH():
    def __init__(self, a, b, p, G):
        self.curve = ECC_curve(a, b, p)
        self.a = a
        self.b = b
        self.p = p

        if not self.curve.is_on_curve(G):
            raise ValueError("G is not on the curve")
        self.G = G

        self.private_key = None
        self.public_key  = None
        self.shared_key  = None

    def gen_private_key(self, d = None):
        if d == None:
            d = self.curve.gen_random_number()
        if d < 0:
            raise ValueError("d should be positive")
        
        self.private_key = d

    def gen_public_key(self):
        if self.private_key == None:
            raise ValueError("private key is not set")

        self.public_key = self.curve.multi(self.G, self.private_key)

    def gen_shared_key(self, Pa):
        if not self.curve.is_on_curve(Pa):
            raise ValueError("Pa is not on the curve")
        if self.private_key == None:
            raise ValueError("private key is not set")

        self.shared_key = self.curve.multi(Pa, self.private_key)
    

def print_point(point):
    print(point[0], point[1], sep=' ', end='\n')

if __name__ == "__main__":
    p = int(input())
    a = int(input())
    b = int(input())

    G = tuple(map(int, input().split()))

    ecdh = ECDH(a, b, p, G)

    d = int(input())
    ecdh.gen_private_key(d)
    ecdh.gen_public_key()

    Pa = tuple(map(int, input().split()))
    ecdh.gen_shared_key(Pa)

    print_point(ecdh.shared_key)
