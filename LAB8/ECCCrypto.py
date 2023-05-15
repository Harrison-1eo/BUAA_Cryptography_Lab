"""
 @description: ECC椭圆曲线加密解密算法
 @author: Harrison-1eo
 @date: 2023-04-29
 @version: 1.0
"""

from ECCCurve import ECC_curve

class ECC_encryptor():
    def __init__(self, a, b, p, G):
        self.curve = ECC_curve(a, b, p)
        self.a = a
        self.b = b
        self.p = p

        if not self.curve.is_on_curve(G):
            raise ValueError("G is not on the curve")
        self.G = G

    def encrypt(self, Pa: tuple, Pm: tuple, k: int) -> tuple:
        if not self.curve.is_on_curve(Pa):
            raise ValueError("Pa is not on the curve")
        if not self.curve.is_on_curve(Pm):
            raise ValueError("Pm is not on the curve")
        if k < 0:
            raise ValueError("k should be positive")

        C1 = self.curve.multi(self.G, k)
        C2 = self.curve.add(Pm, self.curve.multi(Pa, k))

        return C1, C2
    
    def decrypt(self, C1: tuple, C2: tuple, d: int) -> tuple:
        if not self.curve.is_on_curve(C1):
            raise ValueError("C1 is not on the curve")
        if not self.curve.is_on_curve(C2):
            raise ValueError("C2 is not on the curve")
        if d < 0:
            raise ValueError("d should be positive")

        Pm = self.curve.sub(C2, self.curve.multi(C1, d))
        return Pm

def print_point(point):
    print(point[0], point[1], sep=' ', end='\n')

if __name__ == "__main__":

    p = int(input())
    a = int(input())
    b = int(input())

    G = input().split(' ')
    G = (int(G[0]), int(G[1]))

    encryptor = ECC_encryptor(a, b, p, G)

    op = int(input())

    if op == 1:
        Pm = input().split(' ')
        Pm = (int(Pm[0]), int(Pm[1]))
        k  = int(input())
        Pa = input().split(' ')
        Pa = (int(Pa[0]), int(Pa[1]))

        C1, C2 = encryptor.encrypt(Pa, Pm, k)
        print_point(C1)
        print_point(C2)

    elif op == 0:
        C1 = input().split(' ')
        C1 = (int(C1[0]), int(C1[1]))
        C2 = input().split(' ')
        C2 = (int(C2[0]), int(C2[1]))
        d  = int(input())

        Pm = encryptor.decrypt(C1, C2, d)
        print_point(Pm)

    else:
        raise ValueError("Invalid operation")

        




    
        