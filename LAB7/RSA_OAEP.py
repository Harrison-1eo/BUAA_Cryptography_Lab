"""
 @description:  Optimal Asymmetric Encryption Padding
                实现 OAEP 填充规则下的 RSA 算法。
 @author: Harrison-1eo
 @date: 2023-04-15
 @version: 1.0
"""

from RSAutils import quick_mutli, ceil
import hashlib

class RSA_OAEP:
    def __init__(self,hash_func = 'SHA-1'):
        self.hash_func = hash_func

    def hash(self, msg):
        if self.hash_func == 'SHA-1':   
            return hashlib.sha1(msg).digest()

    def byte_length(self, n):
        if n == None:
            return 0
        return int(ceil(n.bit_length() / 8))

    def random_bytes(self, length):
        import random
        return bytes([random.randint(0, 255) for _ in range(length)])

    def AES_encrypt(self, msg: int, n: int, k: int, e: int, seed = None, label = None):
        """
        @description: OAEP 填充下的 AES 加密
        @param {int} msg: 明文
        @param {int} n:   RSA 模数
        @param {int} k:   RSA 密钥长度
        @param {int} e:   RSA 公钥
        @param {int} seed:      伪随机数种子
        @param {bytes} label:   附加信息
        """

        # if seed == None:
        #     seed = self.random_bytes(k - hlen - 1)
        # else:
        #     seed = seed.to_bytes(self.byte_length(seed), 'big')
        seed = seed.to_bytes(self.byte_length(seed), 'big')

        # mlen: 明文长度
        mlen = self.byte_length(msg)
        # 将msg从int转换为bytes
        msg  = msg.to_bytes(mlen, 'big')

        # 计算标签的哈希值及其长度 hlen
        if label == None:
            label = b''
        else:
            if self.byte_length(label) > 0xffffffffffffffff:            # 2^64 - 1
                # raise ValueError("Label too long")
                print("Err")
                exit()
            label = label.to_bytes(self.byte_length(label), 'big')
        lhash = self.hash(label)
        hlen  = len(lhash)

        # OAEP 填充
        msg_encode = self.encode(msg, lhash, seed, mlen, hlen, k)

        # RSA 加密
        return quick_mutli(msg_encode, e, n)

    def encode(self, msg: bytes, lhash: bytes, seed: bytes, mlen: int, hlen: int, k: int):
        """
        @description: OAEP 填充
        @param {bytes} msg:     明文
        @param {bytes} lhash:   附加信息的哈希值
        @param {bytes} seed:    伪随机数种子
        @param {int} mlen:      明文长度
        @param {int} hlen:      附加信息的哈希值长度
        @param {int} k:         RSA 密钥长度
        """

        # 1. 长度检查
        if mlen > k - 2 * hlen - 2:
            # raise ValueError("Message too long")
            print("Err")
            exit()
        
        # 2. 填充
        ps      = b'\x00' * (k - mlen - 2 * hlen - 2)
        db      = lhash + ps + b'\x01' + msg            # db = lhash || ps || 0x01 || m
        
        dbmask  = self.MGF1(seed, k - hlen - 1, hlen)
        masked_db   = bytes([x ^ y for x, y in zip(db, dbmask)])
        seedmask    = self.MGF1(masked_db, hlen, hlen)
        masked_seed = bytes([x ^ y for x, y in zip(seed, seedmask)])
        em =  b'\x00' + masked_seed + masked_db

        # 将中间变量打印出来，用于调试
        # self.log_print(msg = msg, lhash = lhash, ps = ps, db = db, seed = seed, dbmask = dbmask, masked_db = masked_db, seedmask = seedmask, masked_seed = masked_seed, em = em)

        # 将em从bytes转换为int
        return int.from_bytes(em, 'big')
 
    def AES_decrypt(self, msg: int, n: int, k: int, d: int, label = None):
        """
        @description: OAEP 填充下的 AES 解密
        @param {int} msg: 密文
        @param {int} n:   RSA 模数
        @param {int} k:   RSA 密钥长度
        @param {int} d:   RSA 私钥
        @param {bytes} label:   附加信息
        """

        if label == None:
            label = b''
        else:
            if self.byte_length(label) > 0xffffffffffffffff:            # 2^64 - 1
                # raise ValueError("Label too long")
                print("Ree")
                exit()
            label = label.to_bytes(self.byte_length(label), 'big')

        lhash = self.hash(label)
        hlen  = len(lhash)

        if self.byte_length(msg) != k:
            # raise ValueError("Ciphertext length incorrect")
            print("Ree")
            exit()
        
        em = quick_mutli(msg, d, n)
        em = em.to_bytes(k, 'big')

        # RSA 解密
        msg_decode = self.decode(em, lhash, hlen, k)

        return msg_decode
         
    def decode(self, em: bytes, lhash: bytes, hlen: int, k: int):
        """
        @description: OAEP 解码
        @param {bytes} em:      密文
        @param {bytes} lhash:   附加信息的哈希值
        @param {int} hlen:      附加信息的哈希值长度
        @param {int} k:         RSA 密钥长度
        """
        # 1. 长度检查
        if k < 2 * hlen + 2:
            # raise ValueError("Key too short")
            print("Ree")
            exit()
        
        # 2. 解码
        y, masked_seed, masked_db = em[0], em[1:hlen+1], em[hlen+1:]
        if y != 0:
            # raise ValueError("Decoding error, y != 0")
            print("Ree")
            exit()
        seedmask    = self.MGF1(masked_db, hlen, hlen)
        seed        = bytes([x ^ y for x, y in zip(masked_seed, seedmask)])
        dbmask      = self.MGF1(seed, k - hlen - 1, hlen)
        db          = bytes([x ^ y for x, y in zip(masked_db, dbmask)])
        
        lhash_      = db[:hlen]
        if lhash_ != lhash:
            # raise ValueError("Decoding error, lhash_ != lhash")
            print("Ree")
            exit()

        # 去掉前面的0x00
        msg          = db[hlen:].lstrip(b'\x00')
        
        # self.log_print(masked_seed = masked_seed, masked_db = masked_db, db = db, lhash_ = lhash_, msg = msg)
        if msg[0] != 0x01:
            # raise ValueError("Decoding error, msg does not start with 0x01")
            print("Ree")
            exit()
        msg = msg[1:]

        # 将msg从bytes转换为int
        return int.from_bytes(msg, 'big')
        
    def MGF1(self, seed, mask_len, hlen):
        """
        @description: MGF1
        @param {bytes} seed:     种子
        @param {int} mask_len:   生成的掩码长度
        @param {int} hlen:       哈希函数的输出长度
        """
        T = b''
        for counter in range(ceil(mask_len / hlen)):
            C = counter.to_bytes(4, 'big')
            T += self.hash(seed + C)
        return T[:mask_len]

    def log_print(self, **kwargs):
        """
        打印中间变量，用于调试
        """
        # 打印时key值的长度固定输出，左对齐，并且为红色
        for key, value in kwargs.items():
            # value从bytes转换为16进制字符串
            value = bytes.hex(value)
            print('\033[31m{:<10}'.format(key), ':','\033[37m', value)
        return

if __name__ == '__main__':

    op = int(input())       # 1: 加密，0: 解密
    k = int(input())        # 密钥长度
    e = int(input(), 16)    # 加密/解密指数
    N = int(input(), 16)    # 模数
    m = int(input(), 16)    # 明文/密文
    L = input().strip()     # 附加信息
    if L == '0x':
        L = None
    else:
        L = int(L, 16)
    if op == 1:
        seed = int(input(), 16) # 种子

    if op == 1:
        test = RSA_OAEP(hash_func = 'SHA-1')
        c = test.AES_encrypt(m, N, k, e, seed, L)
        # cipher 长度应为 k*2 + 2
        cipher = '0x' + hex(c)[2:].rjust(k*2, '0')
        print(cipher)
