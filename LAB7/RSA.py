"""
 @description: RSA 算法，包括加密、解密、签名、验证。
 @author: Harrison-1eo
 @date: 2023-04-15
 @version: 1.0
"""


from RSAutils import *

class RSA():
    def __init__(self, p = None, q = None, e = None):
        if p is None and q is None:
            self.p, self.q = make_random_key()
            print('p =', self.p)
            print('q =', self.q)
        else:
            self.p, self.q = p, q
        
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        if e is None:
            # self.e = get_random_Nbit_integer(16)
            self.e = 65537
            print('e =', self.e)
        else:
            self.e = e
        self.d = inverse(self.e, self.phi)

    def encrypt(self, x: int):
        return quick_mutli(x, self.e, self.n)

    def decrypt(self, c: int, mode = 'normal'):
        if mode == 'CRT':
            a1 = quick_mutli(c % self.p, self.d % (self.p-1), self.p)
            a2 = quick_mutli(c % self.q, self.d % (self.q-1), self.q)
            return CRT([a1, a2], [self.p, self.q])
        else:
            return quick_mutli(c, self.d, self.n)

    def sign(self, x: int):
        return quick_mutli(x, self.d, self.n)

    def verify(self, c: int):
        return quick_mutli(c, self.e, self.n)
    
    
if __name__ == '__main__':
    p = int(input())
    q = int(input())
    e = int(input())
    rsa = RSA(p, q, e)
    msg = int(input())
    op = input()
    if op == 'encrypt' or op == '1':
        print(rsa.encrypt(msg)) 
    elif op == 'decrypt' or op == '0':
        print(rsa.decrypt(msg), rsa.decrypt(msg, 'CRT'))
    elif op == 'sign' or op == '2':
        print(rsa.sign(msg))
    elif op == 'verify' or op == '3':
        print(rsa.verify(msg))
    else:
        print('Invalid operation')