class _SM4_util:
    CK = [
        0x00070e15, 0x1c232a31, 0x383f464d, 0x545b6269,
        0x70777e85, 0x8c939aa1, 0xa8afb6bd, 0xc4cbd2d9,
        0xe0e7eef5, 0xfc030a11, 0x181f262d, 0x343b4249,
        0x50575e65, 0x6c737a81, 0x888f969d, 0xa4abb2b9,
        0xc0c7ced5, 0xdce3eaf1, 0xf8ff060d, 0x141b2229,
        0x30373e45, 0x4c535a61, 0x686f767d, 0x848b9299,
        0xa0a7aeb5, 0xbcc3cad1, 0xd8dfe6ed, 0xf4fb0209,
        0x10171e25, 0x2c333a41, 0x484f565d, 0x646b7279 ]

    SBOX = [0xD6, 0x90, 0xE9, 0xFE, 0xCC, 0xE1, 0x3D, 0xB7, 0x16, 0xB6, 0x14, 0xC2, 0x28, 0xFB, 0x2C, 0x05,
         0x2B, 0x67, 0x9A, 0x76, 0x2A, 0xBE, 0x04, 0xC3, 0xAA, 0x44, 0x13, 0x26, 0x49, 0x86, 0x06, 0x99,
         0x9C, 0x42, 0x50, 0xF4, 0x91, 0xEF, 0x98, 0x7A, 0x33, 0x54, 0x0B, 0x43, 0xED, 0xCF, 0xAC, 0x62,
         0xE4, 0xB3, 0x1C, 0xA9, 0xC9, 0x08, 0xE8, 0x95, 0x80, 0xDF, 0x94, 0xFA, 0x75, 0x8F, 0x3F, 0xA6,
         0x47, 0x07, 0xA7, 0xFC, 0xF3, 0x73, 0x17, 0xBA, 0x83, 0x59, 0x3C, 0x19, 0xE6, 0x85, 0x4F, 0xA8,
         0x68, 0x6B, 0x81, 0xB2, 0x71, 0x64, 0xDA, 0x8B, 0xF8, 0xEB, 0x0F, 0x4B, 0x70, 0x56, 0x9D, 0x35,
         0x1E, 0x24, 0x0E, 0x5E, 0x63, 0x58, 0xD1, 0xA2, 0x25, 0x22, 0x7C, 0x3B, 0x01, 0x21, 0x78, 0x87,
         0xD4, 0x00, 0x46, 0x57, 0x9F, 0xD3, 0x27, 0x52, 0x4C, 0x36, 0x02, 0xE7, 0xA0, 0xC4, 0xC8, 0x9E,
         0xEA, 0xBF, 0x8A, 0xD2, 0x40, 0xC7, 0x38, 0xB5, 0xA3, 0xF7, 0xF2, 0xCE, 0xF9, 0x61, 0x15, 0xA1,
         0xE0, 0xAE, 0x5D, 0xA4, 0x9B, 0x34, 0x1A, 0x55, 0xAD, 0x93, 0x32, 0x30, 0xF5, 0x8C, 0xB1, 0xE3,
         0x1D, 0xF6, 0xE2, 0x2E, 0x82, 0x66, 0xCA, 0x60, 0xC0, 0x29, 0x23, 0xAB, 0x0D, 0x53, 0x4E, 0x6F,
         0xD5, 0xDB, 0x37, 0x45, 0xDE, 0xFD, 0x8E, 0x2F, 0x03, 0xFF, 0x6A, 0x72, 0x6D, 0x6C, 0x5B, 0x51,
         0x8D, 0x1B, 0xAF, 0x92, 0xBB, 0xDD, 0xBC, 0x7F, 0x11, 0xD9, 0x5C, 0x41, 0x1F, 0x10, 0x5A, 0xD8,
         0x0A, 0xC1, 0x31, 0x88, 0xA5, 0xCD, 0x7B, 0xBD, 0x2D, 0x74, 0xD0, 0x12, 0xB8, 0xE5, 0xB4, 0xB0,
         0x89, 0x69, 0x97, 0x4A, 0x0C, 0x96, 0x77, 0x7E, 0x65, 0xB9, 0xF1, 0x09, 0xC5, 0x6E, 0xC6, 0x84,
         0x18, 0xF0, 0x7D, 0xEC, 0x3A, 0xDC, 0x4D, 0x20, 0x79, 0xEE, 0x5F, 0x3E, 0xD7, 0xCB, 0x39, 0x48
         ]

    def __init__(self):
        pass

    @ classmethod
    def rotate_left(cls, wd, bit):
        return (wd << bit & 0xffffffff) | (wd >> (32 - bit))

    @ classmethod
    def sbox(cls, wd):
        ret = []
        for i in range(0, 4):
            byte = (wd >> (24 - i * 8)) & 0xff
            row = byte >> 4
            col = byte & 0x0f
            index = (row * 16 + col)
            ret.append(cls.SBOX[index])
        ans = 0
        for i in range(0, 4):
            bits = 24 - i * 8
            ans |= ret[i] << bits
        return ans

    @ classmethod
    def T(cls, X1: int, X2: int, X3: int, rk: int):
        t = X1 ^ X2 ^ X3 ^ rk
        t = _SM4_util.sbox(t)
        t = t ^_SM4_util.rotate_left(t, 2) ^ _SM4_util.rotate_left(t, 10) ^ _SM4_util.rotate_left(t, 18) ^ _SM4_util.rotate_left(t, 24)
        return t
    
    @ classmethod
    def R(cls, X0: int, X1: int, X2: int, X3: int):
        X0 &= 0xffffffff
        X1 &= 0xffffffff
        X2 &= 0xffffffff
        X3 &= 0xffffffff
        return X3 << (32*3) | X2 << (32*2) | X1 << (32*1) | X0

    @ classmethod
    def T_key(cls, k1: int, k2: int, k3: int, ck: int):
        xor = k1 ^ k2 ^ k3 ^ ck
        t = _SM4_util.sbox(k1 ^ k2 ^ k3 ^ ck)
        return t ^ _SM4_util.rotate_left(t, 13) ^ _SM4_util.rotate_left(t, 23)

class SM4:
    def __init__(self, key: int):
        self.key = key
        self.rk = self.key_extend(self.key)
    
    def key_extend(self, key: int):
        FK = [0xa3b1bac6, 0x56aa3350, 0x677d9197, 0xb27022dc]
        MK = [key >> (128 - (i + 1) * 32) & 0xffffffff for i in range(4)]
        K  = [FK[i] ^ MK[i] for i in range(4)]
        rk = []
        for i in range(32):
            t = _SM4_util.T_key(K[i + 1], K[i + 2], K[i + 3], _SM4_util.CK[i])
            k = K[i] ^ t
            K.append(k)
            rk.append(k)
        return rk

    def encrypt(self, plaintext: int):
        X = [plaintext >> (128 - (i + 1) * 32) & 0xffffffff for i in range(4)]
        for i in range(32):
            t = _SM4_util.T(X[1], X[2], X[3], self.rk[i])
            c = t ^ X[0]
            X = X[1:] + [c]
        ciphertext = _SM4_util.R(X[0], X[1], X[2], X[3])
        return ciphertext

    def decrypt(self, ciphertext: int):
        X = [ciphertext >> (128 - (i + 1) * 32) & 0xffffffff for i in range(4)]
        for i in range(32):
            t = _SM4_util.T(X[1], X[2], X[3], self.rk[31 - i])
            c = t ^ X[0]
            X = X[1:] + [c]
        plaintext = _SM4_util.R(X[0], X[1], X[2], X[3])
        return plaintext

class SM4_MODE:
    def __init__(self, key: int, parameter = None):
        self.sm4 = SM4(key)
        self.parameter = parameter

    def encrypt(self, plaintext: list, mode: str, initial_vector = None):
        if mode == 'ECB':
            ciphertext = self.ECB_encrypt(plaintext)
        elif mode == 'CBC':
            ciphertext = self.CBC_encrypt(plaintext, initial_vector)
        elif mode == 'CFB':
            ciphertext = self.CFB_encrypt(plaintext, initial_vector)
        elif mode == 'OFB':
            ciphertext = self.OFB_encrypt(plaintext, initial_vector)
        elif mode == 'CTR':
            ciphertext = self.CTR_encrypt(plaintext, initial_vector)
        else:
            print('mode error')
            return None
        return ciphertext
            
    def decrypt(self, ciphertext: list, mode: str, initial_vector = None):
        if mode == 'ECB':
            plaintext = self.ECB_decrypt(ciphertext)
        elif mode == 'CBC':
            plaintext = self.CBC_decrypt(ciphertext, initial_vector)
        elif mode == 'CFB':
            plaintext = self.CFB_decrypt(ciphertext, initial_vector)
        elif mode == 'OFB':
            plaintext = self.OFB_decrypt(ciphertext, initial_vector)
        elif mode == 'CTR':
            plaintext = self.CTR_decrypt(ciphertext, initial_vector)
        else:
            print('mode error')
            return None
        return plaintext
    
    def ECB_encrypt(self, plaintext: list):
        ciphertext = []
        # list中每个元素为2位的str，代表一个字节，每16个字节为一组
        # 计算差值补齐
        
        diff = 16 - len(plaintext) % 16
        plaintext += [hex(diff)[2:].zfill(2)] * diff

        group = []
        for i in range(0, len(plaintext), 16):
            tmp = ''.join(plaintext[i:i+16])
            group.append(int(tmp, 16))

        for i in group:
            # print(group.index(i))
            # print('encrypt', hex(i))
            ans = self.sm4.encrypt(i)
            # print('ans    ', hex(ans))
            ciphertext.append(ans)
        
        ans = []
        for i in ciphertext:
            tmp = hex(i)[2:].zfill(32)
            ans += [tmp[j:j+2] for j in range(0, 32, 2)]
        # ans = [hex(i)[2:].zfill(32)[j:j+2] for i in ciphertext for j in range(0, 32, 2)]

        return ans
    
    def ECB_decrypt(self, ciphertext: list):
        group = []
        for i in range(0, len(ciphertext), 16):
            tmp = ''.join(ciphertext[i:i+16])
            group.append(int(tmp, 16))
        
        plaintext = []
        for i in group:
            # print(group.index(i))
            # print('decrypt', hex(i))
            ans = self.sm4.decrypt(i)
            # print('ans    ', hex(ans))
            plaintext.append(ans)

        ans = []
        for i in plaintext:
            tmp = hex(i)[2:].zfill(32)
            ans += [tmp[j:j+2] for j in range(0, 32, 2)]
        last = int(ans[-1], 16)
        ans = ans[:-last]

        return ans
         
    def CBC_encrypt(self, plaintext: list, initial_vector: int):
        ciphertext = []
        # list中每个元素为2位的str，代表一个字节，每16个字节为一组
        # 计算差值补齐
        
        diff = 16 - len(plaintext) % 16
        plaintext += [hex(diff)[2:].zfill(2)] * diff

        group = []
        for i in range(0, len(plaintext), 16):
            tmp = ''.join(plaintext[i:i+16])
            group.append(int(tmp, 16))
        
        last = initial_vector
        for i in group:
            # print(group.index(i))
            tmp = i ^ last
            # print('encrypt', hex(i))
            ans = self.sm4.encrypt(tmp)
            # print('ans    ', hex(ans))
            ciphertext.append(ans)
            last = ans
        
        ans = []
        for i in ciphertext:
            tmp = hex(i)[2:].zfill(32)
            ans += [tmp[j:j+2] for j in range(0, 32, 2)]
            
        return ans

    def CBC_decrypt(self, ciphertext: list, initial_vector: int):
        group = []
        for i in range(0, len(ciphertext), 16):
            tmp = ''.join(ciphertext[i:i+16])
            group.append(int(tmp, 16))
        
        plaintext = []
        last = initial_vector
        for i in group:
            # print(group.index(i))
            # print('decrypt', hex(i))
            ans = self.sm4.decrypt(i)
            # print('ans    ', hex(ans))
            plaintext.append(ans ^ last)
            last = i

        ans = []
        for i in plaintext:
            tmp = hex(i)[2:].zfill(32)
            ans += [tmp[j:j+2] for j in range(0, 32, 2)]
        last = int(ans[-1], 16)
        ans = ans[:-last]

        return ans

    def CTR_encrypt(self, plaintext: list, initial_vector: int):
        ciphertext = []
        # list中每个元素为2位的str，代表一个字节，每16个字节为一组
        # 计算差值补齐
        
        diff = 16 - len(plaintext) % 16
        plaintext += ['00'] * diff

        group = []
        for i in range(0, len(plaintext), 16):
            tmp = ''.join(plaintext[i:i+16])
            group.append(int(tmp, 16))
        
        for index, i in enumerate(group):
            tmp = self.sm4.encrypt(initial_vector + index)
            # print(group.index(i))
            # print('encrypt', hex(i))
            ans = i ^ tmp
            # print('ans    ', hex(ans))
            ciphertext.append(ans)
        
        ans = []
        for i in ciphertext:
            tmp = hex(i)[2:].zfill(32)
            ans += [tmp[j:j+2] for j in range(0, 32, 2)]
            
        return ans[:-diff]

    def CTR_decrypt(self, ciphertext: list, initial_vector: int):
        diff = 16 - len(ciphertext) % 16
        ciphertext += ['00'] * diff
        
        group = []
        for i in range(0, len(ciphertext), 16):
            tmp = ''.join(ciphertext[i:i+16])
            group.append(int(tmp, 16))
        
        plaintext = []
        for index, i in enumerate(group):
            tmp = self.sm4.encrypt(initial_vector + index)
            # print(group.index(i))
            # print('decrypt', hex(i))
            ans = i ^ tmp
            # print('ans    ', hex(ans))
            plaintext.append(ans)

        ans = []
        for i in plaintext:
            tmp = hex(i)[2:].zfill(32)
            ans += [tmp[j:j+2] for j in range(0, 32, 2)]
        
        return ans[ :-diff]

    def CFB_encrypt(self, plaintext: list, initial_vector: int):

        round = self.parameter['round']
        reg = initial_vector

        diff = round - len(plaintext) % round
        plaintext += ['00'] * diff

        group = []
        for i in range(0, len(plaintext), round):
            tmp = ''.join(plaintext[i:i+round])
            group.append(int(tmp, 16))

        ciphertext = []
        for i in group:
            K = self.sm4.encrypt(reg)
            # print(group.index(i), hex(reg), hex(K))
            # K 128位，取出前round个字节
            tmp = K >> (128 - round * 8)
            ans = i ^ tmp
            # print(hex(i), hex(tmp), hex(ans))
            ciphertext.append(ans)
            reg = ((reg << round * 8) | ans) & 0xffffffffffffffffffffffffffffffff

        ans = []
        char = ''
        for i in ciphertext:
            char += hex(i)[2:].zfill(round * 2)
        
        for i in range(0, len(char), 2):
            ans.append(char[i:i+2])
        
        return ans[:-diff]

    def CFB_decrypt(self, ciphertext: list, initial_vector: int):
        round = self.parameter['round']
        reg = initial_vector

        diff = round - len(ciphertext) % round
        ciphertext += ['00'] * diff

        group = []
        for i in range(0, len(ciphertext), round):
            tmp = ''.join(ciphertext[i:i+round])
            group.append(int(tmp, 16))

        plaintext = []
        for i in group:
            K = self.sm4.encrypt(reg)
            # K 128位，取出前round个字节
            tmp = K >> (128 - round * 8)
            ans = i ^ tmp
            plaintext.append(ans)
            reg = ((reg << round * 8) | i) & 0xffffffffffffffffffffffffffffffff

        ans = []
        char = ''
        for i in plaintext:
            char += hex(i)[2:].zfill(round * 2)
        
        for i in range(0, len(char), 2):
            ans.append(char[i:i+2])
        
        return ans[:-diff]

    def OFB_encrypt(self, plaintext: list, initial_vector: int):

        round = self.parameter['round']
        reg = initial_vector

        diff = round - len(plaintext) % round
        plaintext += ['00'] * diff

        group = []
        for i in range(0, len(plaintext), round):
            tmp = ''.join(plaintext[i:i+round])
            group.append(int(tmp, 16))

        ciphertext = []
        for i in group:
            K = self.sm4.encrypt(reg)
            # print(group.index(i), hex(reg), hex(K))
            # K 128位，取出前round个字节
            tmp = K >> (128 - round * 8)
            ans = i ^ tmp
            # print(hex(i), hex(tmp), hex(ans))
            ciphertext.append(ans)
            reg = ((reg << round * 8) | tmp) & 0xffffffffffffffffffffffffffffffff

        ans = []
        char = ''
        for i in ciphertext:
            char += hex(i)[2:].zfill(round * 2)
        
        for i in range(0, len(char), 2):
            ans.append(char[i:i+2])
        
        return ans[:-diff]

    def OFB_decrypt(self, ciphertext: list, initial_vector: int):
        round = self.parameter['round']
        reg = initial_vector

        diff = round - len(ciphertext) % round
        ciphertext += ['00'] * diff

        group = []
        for i in range(0, len(ciphertext), round):
            tmp = ''.join(ciphertext[i:i+round])
            group.append(int(tmp, 16))

        plaintext = []
        for i in group:
            K = self.sm4.encrypt(reg)
            # K 128位，取出前round个字节
            tmp = K >> (128 - round * 8)
            ans = i ^ tmp
            plaintext.append(ans)
            reg = ((reg << round * 8) | tmp) & 0xffffffffffffffffffffffffffffffff

        ans = []
        char = ''
        for i in plaintext:
            char += hex(i)[2:].zfill(round * 2)
        
        for i in range(0, len(char), 2):
            ans.append(char[i:i+2])
        
        return ans[:-diff]


def main(mode: str):
    param = {}
    if mode == 'CFB' or mode == 'OFB':
        round = int(input())
        param['round'] = round
    key = int(input(), 16)
    iv = None
    if mode == 'CBC' or mode == 'CTR' or mode == 'CFB' or mode == 'OFB':
        iv = int(input(), 16)
    op = int(input())
    msg = []
    while True:
        try:
            a = input().split()
            msg += a
        except:
            break
    
    msg_2bits = []
    for i in msg:
        msg_2bits.append(i[2:])
    run = SM4_MODE(key, param)
    
    if op == 0:
        ciphertext = run.decrypt(msg_2bits, mode, iv)
    else:
        ciphertext = run.encrypt(msg_2bits, mode, iv)
    
    j = 0 
    for i in ciphertext:
        print('0x' + i, end=' ')
        j += 1
        if j % 16 == 0:
            print()

if __name__ == "__main__":
    main('OFB')

    