"""
 @description: SM3算法实现
 @author: Harrison-1eo
 @date: 2023-05-04
 @version: 1.0
"""


import struct

class SM3:
    def __init__(self) -> None:
        pass

    def padding(self, msg: bytes) -> bytes:
        """
        @description: SM3填充函数
        @param {bytes} msg: 待填充的消息
        @return {bytes} 填充后的消息
        """

        mlen = len(msg) * 8
        msg += b'\x80'
        while len(msg) % 64 != 56:
            msg += b'\x00'
        msg += struct.pack('>Q', mlen)
        return msg
    
    def left_rotate(self, x, n):
        """
        @description: 循环左移函数
        @param {int} x: 待移位的数
        @param {int} n: 移位数
        @return {int} 移位后的数
        """
        return ((x << n) | (x >> (32 - n))) & 0xffffffff
    
    def P0(self, x):
        """
        @description: 置换函数P0
        """
        return x ^ self.left_rotate(x, 9) ^ self.left_rotate(x, 17)
    
    def P1(self, x):
        """
        @description: 置换函数P1
        """
        return x ^ self.left_rotate(x, 15) ^ self.left_rotate(x, 23)

    def F1(self, x, y, z):
        """
        @description: 置换函数FF, 前16轮
        """
        return x ^ y ^ z
    
    def F2(self, x, y, z):
        """
        @description: 置换函数FF, 后48轮
        """
        return (x & y) | (x & z) | (y & z)

    def G1(self, x, y, z):
        """
        @description: 置换函数GG, 前16轮
        """
        return x ^ y ^ z
    
    def G2(self, x, y, z):

        return (x & y) | (~x & z)
    

    def extend(self, msg: bytes):
        if len(msg) != 64:
            raise ValueError('msg length must be 64 bytes')
        w  = [0] * 68
        ww = [0] * 64
        for i in range(16):
            w[i] = int.from_bytes(msg[i*4: i*4+4], 'big')
        for i in range(16, 68):
            w[i] = self.P1(w[i-16] ^ w[i-9] ^ self.left_rotate(w[i-3], 15)) ^ self.left_rotate(w[i-13], 7) ^ w[i-6]
        for i in range(64):
            ww[i] = w[i] ^ w[i+4]
        return w, ww

    def compress(self, block, v):
        Tj = [0x79cc4519, 0x7a879d8a]
        a, b, c, d, e, f, g, h = v
        w, ww = self.extend(block)
        for i in range(64):
            t = (Tj[0] if i < 16 else Tj[1])
            ss1 = self.left_rotate((self.left_rotate(a, 12) + e + self.left_rotate(t, i % 32)) &  0xffffffff, 7)
            ss2 = ss1 ^ self.left_rotate(a, 12)
            tt1 = (self.F1(a, b, c) if i < 16 else self.F2(a, b, c)) + d + ss2 + ww[i] & 0xffffffff
            tt2 = (self.G1(e, f, g) if i < 16 else self.G2(e, f, g)) + h + ss1 + w[i]  & 0xffffffff
            d = c
            c = self.left_rotate(b, 9)
            b = a
            a = tt1
            h = g
            g = self.left_rotate(f, 19)
            f = e
            e = self.P0(tt2) & 0xffffffff

            # print(i, hex(a), hex(b), hex(c), hex(d), hex(e), hex(f), hex(g), hex(h))
        alpha = [a, b, c, d, e, f, g, h]
        v = [x ^ y for x, y in zip(v, alpha)]
        return v

    # 主函数，计算SM3哈希值
    def sm3(self, message: bytes) -> str:
        IV = [0x7380166f, 0x4914b2b9, 0x172442d7, 0xda8a0600, 0xa96f30bc, 0x163138aa, 0xe38dee4d, 0xb0fb0e4e]
        message = self.padding(message)
        n = len(message)
        # 512位为一块，迭代压缩函数
        v = IV.copy()
        for i in range(n // 64):
            block = message[i*64:i*64+64]
            v = self.compress(block, v)
        return '%08x%08x%08x%08x%08x%08x%08x%08x' % tuple(v)


if __name__ == '__main__':
    sm3 = SM3()
    msg = input().split('\n')[0].encode('utf-8')
    
    print(sm3.sm3(msg))