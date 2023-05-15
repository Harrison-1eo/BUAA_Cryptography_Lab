_AesFaultPtr = [[0, 13, 10, 7],[4, 1, 14, 11],[8, 5, 2, 15],[12, 9, 6, 3]]

_AesMixColumns = [[2, 3, 1, 1],[1, 2, 3, 1],[1, 1, 2, 3],[3, 1, 1, 2]]

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

    @classmethod
    def key_trans(cls, a0, r):
        a0 = ((a0 << 8) + (a0 >> 24)) & ((1 << 32) - 1)
        a0 = cls.SBOX[(a0 & ((1 << 8) - 1)) // 16][(a0 & ((1 << 8) - 1)) % 16] + (
                cls.SBOX[((a0 >> 8) & ((1 << 8) - 1)) // 16][((a0 >> 8) & ((1 << 8) - 1)) % 16] << 8) + (
                    cls.SBOX[((a0 >> 16) & ((1 << 8) - 1)) // 16][((a0 >> 16) & ((1 << 8) - 1)) % 16] << 16) + (
                    (cls.SBOX[((a0 >> 24) & ((1 << 8) - 1)) // 16][((a0 >> 24) & ((1 << 8) - 1)) % 16] << 24) ^ r)
        return a0

    @classmethod
    def solve_key10(cls, K10):
        R = [0x01000000, 0x02000000, 0x04000000, 0x08000000, 0x10000000, 0x20000000, 0x40000000, 0x80000000, 0x1b000000,
     0x36000000]
        K = [0] * 44
        K[40] = (K10[0][0] << 24) + (K10[1][0] << 16) + (K10[2][0] << 8) + K10[3][0]
        K[41] = (K10[0][1] << 24) + (K10[1][1] << 16) + (K10[2][1] << 8) + K10[3][1]
        K[42] = (K10[0][2] << 24) + (K10[1][2] << 16) + (K10[2][2] << 8) + K10[3][2]
        K[43] = (K10[0][3] << 24) + (K10[1][3] << 16) + (K10[2][3] << 8) + K10[3][3]
        for i in range(40):
            if i % 4 != 3:
                K[39 - i] = K[43 - i] ^ K[42 - i]
            else:
                K[39 - i] = K[43 - i] ^ cls.key_trans(K[42 - i], R[9 - (i // 4)])
        k = (K[0] << 96) + (K[1] << 64) + (K[2] << 32) + K[3]
        return k


def getDiff(output, mode):
    diff = output ^ ciphertext
    tmp = bin(diff)[2:].rjust(128, '0')
    ans = []
    for j in range(4):
        i = _AesFaultPtr[mode][j]
        ans.append(int(tmp[i * 8: i * 8 + 8], 2))
    return ans

def crack():
    r9state = [[0 for i in range(4)] for j in range(4)]
    
    for i in range(4):
        optionlist = []
        for j in range(10):
            diff = getDiff(r9faults[i * 10 + j], i)
            if optionlist == []:
                optionlist = calculatePossibleValues(diff)
            else:
                optionlist = filterPossibleValues(diff, optionlist)

        for j in range(4):
            r9state[j][i] = optionlist[0][j]

        # print(r9state)
    
    state    = _AES_util.sub_bytes(r9state)
    state    = _AES_util.shift_rows(state)
    r10state = _AES_util.convert_to_matrix(hex(ciphertext)[2:].rjust(32, '0'))
    k10      = _AES_util.add_round_key(state, r10state)
    return _AES_util.solve_key10(k10)                     


def calculatePossibleValues(diff):
    mulCof = [2, 1, 1, 3]
    ans = []
    for e in range(1, 256):
        pos = [[], [], [], []]
        for x0 in range(256):
            for j in range(4):
                if _AES_util.sbox(x0 ^ _AES_util.mul(mulCof[j], e)) == _AES_util.sbox(x0) ^ diff[j]:
                    pos[j].append(x0)

        for x_0 in pos[0]:
            for x_1 in pos[1]:
                for x_2 in pos[2]:
                    for x_3 in pos[3]:
                        ans.append((x_0, x_1, x_2, x_3))
    
    return ans

def filterPossibleValues(diff, candidates):
    mulCof = [2, 1, 1, 3]
    ans = []
    for candi in candidates:
        for e in range(1, 256):
            flag = True
            for j in range(4):
                if _AES_util.sbox(candi[j] ^ _AES_util.mul(mulCof[j], e)) != _AES_util.sbox(candi[j]) ^ diff[j]:
                    flag = False
                    break
            if flag:
                ans.append(candi)
                break
  
    return ans

if __name__ == '__main__':
    times = 160
    plaintext  = input().strip()

    ciphertext = int(input().strip(), 16)
    r9faults   = [int(input().strip(), 16) for _ in range(times)]

    ans = crack()
    print('0x' + hex(ans)[2:].rjust(32, '0'))