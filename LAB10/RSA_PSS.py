"""
 @project: RSA_PSS.py
 @description:  实现 RSA-PSS 数字签名算法。
                本题所用哈希函数固定为SHA1，即 hLen=20；
                本题所有盐值固定为 20 字节，即 sLen=20；
                本题采用模数的比特长度固定为 1024。
 @author: Harrison-1eo
 @date: 2023-05-21
 @version: 1.0
"""
from hashlib import sha1
from math import ceil


class RSA_PSS:
    def __init__(self, d, e, N, hash_func='SHA-1'):
        self.d = d
        self.e = e
        self.N = N
        self.hash_func = hash_func
        
    def _hash(self, msg: bytes) -> bytes:
        if self.hash_func == 'SHA-1':   
            return sha1(msg).digest()
    
    def _hash_len(self) -> int:
        if self.hash_func == 'SHA-1':
            return 20
      
    def _MGF1(self, seed, mask_len, hlen):
        """
        @description: MGF1
        @param {bytes} seed:     种子
        @param {int} mask_len:   生成的掩码长度
        @param {int} hlen:       哈希函数的输出长度
        """
        T = b''
        for counter in range(ceil(mask_len / hlen)):
            C = counter.to_bytes(4, 'big')
            T += self._hash(seed + C)
        return T[:mask_len]
      
    def encode(self, msg: bytes, em_bits: int, salt: bytes) -> int:
        s_len = 20
        h_len = self._hash_len()
        em_len = ceil(em_bits / 8)

        # 内置hash函数只支持不可变对象，所以这里用bytes
        m_hash = self._hash(msg)

        padding1 = b'\x00' * 8
        padding2 = b'\x00' * (em_len - s_len - h_len - 2) + b'\x01'

        M = padding1 + m_hash + salt
        H = self._hash(M)
        

        db = padding2 + salt
        
        db_mask = self._MGF1(H, em_len - h_len - 1, h_len)
        # bytearray是可变对象，所以这里用bytearray
        masked_db = bytearray([db[i] ^ db_mask[i] for i in range(em_len - h_len - 1)])
        
        masked_db[0] = masked_db[0] & (0xff >> (8 * em_len - em_bits))
        
        em = masked_db + H + b'\xbc'

        return int.from_bytes(em, 'big')
    
    def sign(self, msg: bytes, em_bits: int, salt: bytes) -> int:
        """
        签名函数
        :param msg:  消息
        :param em_bits:  em的比特长度
        :param salt:  盐值
        :return: 签名后的消息
        """
        em = self.encode(msg, em_bits, salt)
        return pow(em, self.d, self.N)

    def verify(self, msg: bytes, signature: int, em_bits: int) -> bool:
        """
        验证函数
        :param msg:  消息
        :param signature:  签名后的消息
        :param em_bits:  em的比特长度
        :return:  验证结果
        """
        s_len = 20
        h_len = self._hash_len()
        em_len = ceil(em_bits / 8)

        padding1 = b'\x00' * 8
        padding2 = b'\x00' * (em_len - s_len - h_len - 2) + b'\x01'

        m = pow(signature, self.e, self.N)
        em = m.to_bytes(em_len, 'big')

        m_hash = self._hash(msg)

        if em_len < h_len + s_len + 2:
            raise ValueError('inconsistent em_len')

        if em[-1] != 0xbc:
            raise ValueError('inconsistent em')

        masked_db = em[:em_len - h_len - 1]
        H = em[em_len - h_len - 1: - 1]

        if masked_db[0] & (0xff << (8 - em_len * 8 + em_bits)):
            raise ValueError('inconsistent masked_db')

        db_mask = self._MGF1(H, em_len - h_len - 1, h_len)
        db = bytearray([masked_db[i] ^ db_mask[i] for i in range(em_len - h_len - 1)])
        db[0] = db[0] & (0xff >> (8 * em_len - em_bits))

        if db[:em_len - h_len - s_len - 1] != padding2:
            raise ValueError('inconsistent padding2')

        salt = db[-s_len:]
        M = padding1 + m_hash + salt

        if H != self._hash(M):
            raise ValueError('inconsistent H')
        else:
            return True


if __name__ == '__main__':
    message = input().encode('utf-8')
    n = int(input())
    em_bits = int(input())
    mode = input().strip().lower()
    if mode == 'sign':
        d = int(input())
        salt_ = bytes.fromhex(input())
        rsa = RSA_PSS(d, None, n)
        signature = rsa.sign(message, em_bits, salt_)
        print(hex(signature)[2:])
    elif mode == 'vrfy':
        e = int(input())
        signature = int(input(), 16)
        rsa = RSA_PSS(None, e, n)
        try:
            rsa.verify(message, signature, em_bits)
            print('True')
        except ValueError as e:
            print('False')
            # print(e)
    else:
        raise ValueError('mode error')