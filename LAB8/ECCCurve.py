"""
 @description: ECC椭圆曲线基本运算
 @author: Harrison-1eo
 @date: 2023-04-29
 @version: 1.0
"""

import random


class ECC_curve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
    
    def print_curve(self):
        print("y^2 = x^3 + {}x + {}".format(self.a, self.b))

    def is_on_curve(self, A: tuple):
        x, y = A
        return (y * y - x * x * x - self.a * x - self.b) % self.p == 0

    def add(self, A: tuple, B: tuple):
        x1, y1 = A
        x2, y2 = B
        if x1 == x2 and y1 == y2:
            if y1 == 0:
                return 0, 0
            else:
                k = (3 * x1 * x1 + self.a) * pow(2 * y1, self.p - 2, self.p)
        else:
            k = (y2 - y1) * pow(x2 - x1, self.p - 2, self.p)
        x3 = (k * k - x1 - x2) % self.p
        y3 = (k * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def multi(self, A: tuple, k: int):
        if k == 0:
            return (0, 0)
        elif k == 1:
            return A
        elif k % 2 == 0:
            return self.multi(self.add(A, A), k // 2)
        else:
            return self.add(self.multi(A, k - 1), A)

    def sub(self, A: tuple, B: tuple):
        x1, y1 = A
        x2, y2 = B
        if x1 == x2 and y2 == y1:
            return (0, 0)
        return self.add(A, (B[0], -B[1] % self.p))

    def gen_random_point(self):
        while True:
            x = random.randint(0, self.p - 1)
            y = random.randint(0, self.p - 1)
            if self.is_on_curve((x, y)):
                return (x, y)

    def gen_random_number(self):
        return random.randint(1, self.p - 1)

    def int_to_bytes(self, x: int) -> bytes:
        return int.to_bytes(x, (x.bit_length() + 7) // 8, 'big')


def print_point(point):
    print(point[0], point[1], sep=' ', end='\n')


if __name__ == "__main__":
    p = int(input())
    a = int(input())
    b = int(input())

    A = input().split(' ')
    B = input().split(' ')

    k = int(input())

    A = [int(i) for i in A]
    B = [int(i) for i in B]

    ecc = ECC_curve(a, b, p)

    print_point(ecc.add(A, B))
    print_point(ecc.sub(A, B))
    print_point(ecc.multi(A, k))
