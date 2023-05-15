
class _AES_util():
    SBOX = [
        [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
        [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
        [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
        [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
        [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
        [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
        [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
        [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
        [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
        [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
        [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
        [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
        [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
        [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
        [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
        [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]

    SBOX_INV = [
        [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
        [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
        [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
        [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
        [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
        [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
        [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
        [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
        [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
        [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
        [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
        [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
        [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
        [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
        [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
        [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]]

    def __init__(self) -> None:
        pass

    @classmethod
    def key_convert_to_matrix(cls, text, num):
        matrix = [[0 for i in range(4)] for j in range(num)]
        ptr = 0
        for i in range(num):
            for j in range(4):
                m = text[ptr] + text[ptr+1]
                matrix[i][j] = int(m, 16)
                ptr += 2
        # print(matrix)
        return matrix
    
    @classmethod
    def key_final(cls, key: list):
        matrix = []
        for k in range(len(key)//4):
            a = [[0 for i in range(4)] for j in range(4)]
            for i in range(4):
                for j in range(4):
                    a[j][i] = key[4*k+i][j]
            matrix.append(a)
        return matrix

    @classmethod
    def sbox(cls, word: int):
        row = word >> 4
        column = word & 0x0f
        return cls.SBOX[row][column]

    # convert the 32 bit string to 4x4 int matrix
    @classmethod
    def convert_to_matrix(cls, text):
        matrix = [[0 for i in range(4)] for j in range(4)]
        ptr = 0
        for i in range(4):
            for j in range(4):
                m = text[ptr] + text[ptr+1]
                matrix[j][i] = int(m, 16)
                ptr += 2
        # print(matrix)
        return matrix

    # convert the 4x4 int matrix to 32 bit string
    @classmethod
    def convert_to_string(cls, matrix):
        text = ""
        for i in range(4):
            for j in range(4):
                text += hex(matrix[j][i])[2:].rjust(2, '0')
        # print(text)
        return text

    # add round key
    @classmethod
    def add_round_key(cls, state, key):
        for i in range(4):
            for j in range(4):
                state[i][j] = state[i][j] ^ key[i][j]
        # print(state)
        return state

    # sub bytes
    @classmethod
    def sub_bytes(cls, state):
        for i in range(4):
            for j in range(4):
                row = state[i][j] >> 4
                column = state[i][j] & 0x0f
                state[i][j] = cls.SBOX[row][column]
        return state

    # shift rows
    @classmethod
    def shift_rows(cls, state):
        for i in range(1, 4):
            state[i] = state[i][i:] + state[i][:i]
        return state

    # multiply two numbers in GF(2^8)
    @classmethod
    def mul(cls, a, b):
        p = 0
        hi_bit_set = 0
        for i in range(8):
            if b & 1 == 1:
                p ^= a

            hi_bit_set = a & 0x80
            a <<= 1
            if hi_bit_set == 0x80:
                a ^= 0x1b
            b >>= 1
        return p % 256

    # mix columns
    @classmethod
    def mix_columns(cls, state):
        new_state = [[], [], [], []]

        for i in range(4):
            new_state[0].append(cls.mul(0x02, state[0][i]) ^ cls.mul(0x03, state[1][i]) ^ state[2][i] ^ state[3][i])
            new_state[1].append(state[0][i] ^ cls.mul(0x02, state[1][i]) ^ cls.mul(0x03, state[2][i]) ^ state[3][i])
            new_state[2].append(state[0][i] ^ state[1][i] ^ cls.mul(0x02, state[2][i]) ^ cls.mul(0x03, state[3][i]))
            new_state[3].append(cls.mul(0x03, state[0][i]) ^ state[1][i] ^ state[2][i] ^ cls.mul(0x02, state[3][i]))

        return new_state

    # inverse sub bytes
    @classmethod
    def inv_sub_bytes(cls, state):
        for i in range(4):
            for j in range(4):
                row = state[i][j] >> 4
                column = state[i][j] & 0x0f
                state[i][j] = cls.SBOX_INV[row][column]
        return state
    
    # inverse shift rows
    @classmethod
    def inv_shift_rows(cls, state):
        for i in range(1, 4):
            state[i] = state[i][-i:] + state[i][:-i]
        return state
    
    # inverse mix columns
    @classmethod
    def inv_mix_columns(cls, state):
        new_state = [[], [], [], []]
        for i in range(4):
            new_state[0].append(cls.mul(0x0e, state[0][i]) ^ cls.mul(0x0b, state[1][i]) ^ cls.mul(0x0d, state[2][i]) ^ cls.mul(0x09, state[3][i]))
            new_state[1].append(cls.mul(0x09, state[0][i]) ^ cls.mul(0x0e, state[1][i]) ^ cls.mul(0x0b, state[2][i]) ^ cls.mul(0x0d, state[3][i]))
            new_state[2].append(cls.mul(0x0d, state[0][i]) ^ cls.mul(0x09, state[1][i]) ^ cls.mul(0x0e, state[2][i]) ^ cls.mul(0x0b, state[3][i]))
            new_state[3].append(cls.mul(0x0b, state[0][i]) ^ cls.mul(0x0d, state[1][i]) ^ cls.mul(0x09, state[2][i]) ^ cls.mul(0x0e, state[3][i]))
        return new_state

class AES(_AES_util):
    def __init__(self, key: str):
        self.mode = len(key) * 4           # self.mode: int
        self.key = key                     # self.key : str
        self.subkey = self._key_expansion(key)
        # Nr: 加密轮数，值为10、12、14
        self.Nr = 10 + (self.mode - 128) // 32

    def _key_expansion(self, key: str):
        Rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]
        # Nr: 密钥拓展轮数，值为10、12、14
        Nr = 10 + (self.mode - 128) // 32
        # Nk: 密钥长度，值为4、6、8
        Nk = self.mode // 32
        # w: 密钥拓展结果，长度为4 * (Nr + 1)，存储类型为int
        w = [[0 for i in range(4)] for j in range(4 * (Nr+1))]

        key_m0 = _AES_util.key_convert_to_matrix(key, Nk)

        for i in range(Nk):
            w[i] = key_m0[i]
        
        for i in range(Nk, 4 * (Nr+1)):
            temp = w[i-1]
            if i % Nk == 0:
                temp = [temp[1], temp[2], temp[3], temp[0]]
                temp = [_AES_util.sbox(temp[j]) for j in range(4)]
                temp[0] ^= Rcon[i//Nk - 1]
            elif Nk > 6 and i % Nk == 4:
                temp = [_AES_util.sbox(temp[j]) for j in range(4)]
            w[i] = [ w[i - Nk][j] ^ temp[j] for j in range(4) ]
        
        return _AES_util.key_final(w)

    def _get_subkey(self, i: int):
        # for i in range(len(self.subkey)):
        #     print(i, self.subkey[i])
        return self.subkey[i]
    
    def encrypt(self, plaintext: str):
        """AES encryption algorithm
        plaintext is a 32-byte string
        during testing, the type of plaintext and key is int 
        """
        # convert plaintext and key to 4x4 matrix
        plaintext = _AES_util.convert_to_matrix(plaintext)
        # add round key
        state = _AES_util.add_round_key(plaintext, self._get_subkey(0))
        
        # 9 rounds
        for i in range(self.Nr-1):
            state = _AES_util.sub_bytes(state)                                  # 字节代替
            state = _AES_util.shift_rows(state)                                 # 行移位
            state = _AES_util.mix_columns(state)                                # 列混淆
            state = _AES_util.add_round_key(state, self._get_subkey(i+1))       # 轮密钥加
        
        # final round
        state = _AES_util.sub_bytes(state)
        state = _AES_util.shift_rows(state)
        state = _AES_util.add_round_key(state, self._get_subkey(self.Nr))

        # convert state to string
        ciphertext = _AES_util.convert_to_string(state)
        return ciphertext

    def decrypt(self, ciphertext: str):
        """AES decryption algorithm
        ciphertext is a 32-byte string
        """
        # convert ciphertext and key to 4x4 matrix
        ciphertext = _AES_util.convert_to_matrix(ciphertext)
        # add round key
        state = _AES_util.add_round_key(ciphertext, self._get_subkey(self.Nr))
        
        # 9 rounds
        for i in range(self.Nr-1):
            state = _AES_util.inv_shift_rows(state)
            state = _AES_util.inv_sub_bytes(state)
            state = _AES_util.add_round_key(state, self._get_subkey(self.Nr-i-1))
            state = _AES_util.inv_mix_columns(state)
        
        # final round
        state = _AES_util.inv_shift_rows(state)
        state = _AES_util.inv_sub_bytes(state)
        state = _AES_util.add_round_key(state, self._get_subkey(0))

        # convert state to string
        plaintext = _AES_util.convert_to_string(state)
        return plaintext


def main():
    # keylen = int(input())
    num = int(input())
    msg = input().strip()[2:]
    key = input().strip()[2:]
    mode = int(input())
    aes = AES(key)
    if mode == 0:
        for i in range(num):
            msg = aes.decrypt(msg)
    else:
        for i in range(num):
            msg = aes.encrypt(msg)
    print('0x'+msg)
    
if __name__ == '__main__':
    main()