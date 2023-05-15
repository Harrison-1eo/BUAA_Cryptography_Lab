"""
 @description: SHA-1算法实现
 @author: Harrison-1eo
 @date: 2023-05-04
 @version: 1.0
"""


import struct


# 循环左移函数
def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff


# SHA-1算法主要函数
def sha1(message: bytes):
    # 初始化5个32位的变量，用于存储哈希值
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # 对消息进行填充，使其长度为64的倍数
    ml = len(message) * 8
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += struct.pack('>Q', ml)

    # 处理消息，每次处理64字节
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        w = [0] * 80
        for j in range(16):
            w[j] = struct.unpack('>I', chunk[j * 4:j * 4 + 4])[0]
        for j in range(16, 80):
            w[j] = left_rotate((w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16]), 1)
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        for j in range(80):
            if j < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif j < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif j < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            temp = left_rotate(a, 5) + f + e + k + w[j] & 0xffffffff
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp
        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    # 将5个32位的变量拼接成160位的哈希值
    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)


if __name__ == '__main__':
    msg = input().strip()
    print(sha1(msg.encode('utf-8')))
