KEY_PC1 =  [57, 49, 41, 33, 25, 17,  9,  1, 58, 50, 42, 34, 26, 18,
            10,  2, 59, 51, 43, 35, 27, 19, 11,  3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,  7, 62, 54, 46, 38, 30, 22,
            14,  6, 61, 53, 45, 37, 29, 21, 13,  5, 28, 20, 12,  4]
KEY_PC2 =  [14, 17, 11, 24,  1,  5,  3, 28, 15,  6, 21, 10,
            23, 19, 12,  4, 26,  8, 16,  7, 27, 20, 13,  2,
            41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
SHIFT =    [ 1,  1,  2,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  2,  1]
FP =       [40,  8, 48, 16, 56, 24, 64, 32, 39,  7, 47, 15, 55, 23, 63, 31,
            38,  6, 46, 14, 54, 22, 62, 30, 37,  5, 45, 13, 53, 21, 61, 29,
            36,  4, 44, 12, 52, 20, 60, 28, 35,  3, 43, 11, 51, 19, 59, 27,
            34,  2, 42, 10, 50, 18, 58, 26, 33,  1, 41,  9, 49, 17, 57, 25]
SP_Box = [
        [0x00410100, 0x00000000, 0x00010000, 0x40410100,
        0x40010100, 0x40410000, 0x40000000, 0x00010000,
        0x00400000, 0x00410100, 0x40410100, 0x00400000,
        0x40400100, 0x40010100, 0x00000100, 0x40000000,
        0x40400000, 0x00400100, 0x00400100, 0x00410000,
        0x00410000, 0x00010100, 0x00010100, 0x40400100,
        0x40010000, 0x40000100, 0x40000100, 0x40010000,
        0x00000000, 0x40400000, 0x40410000, 0x00000100,
        0x00010000, 0x40410100, 0x40000000, 0x00010100,
        0x00410100, 0x00000100, 0x00000100, 0x00400000,
        0x40010100, 0x00010000, 0x00410000, 0x40000100,
        0x00400000, 0x40000000, 0x40400100, 0x40410000,
        0x40410100, 0x40010000, 0x00010100, 0x40400100,
        0x40000100, 0x40400000, 0x40410000, 0x00410100,
        0x40400000, 0x00400100, 0x00400100, 0x00000000,
        0x40010000, 0x00410000, 0x00000000, 0x40010100],

        [0x08021002, 0x00020002, 0x00020000, 0x08021000,
        0x00001000, 0x08000000, 0x08001002, 0x08020002,
        0x08000002, 0x08021002, 0x00021002, 0x00000002,
        0x00020002, 0x00001000, 0x08000000, 0x08001002,
        0x00021000, 0x08001000, 0x08020002, 0x00000000,
        0x00000002, 0x00020000, 0x08021000, 0x00001002,
        0x08001000, 0x08000002, 0x00000000, 0x00021000,
        0x08020000, 0x00021002, 0x00001002, 0x08020000,
        0x00000000, 0x08021000, 0x08001002, 0x00001000,
        0x08020002, 0x00001002, 0x00021002, 0x00020000,
        0x00001002, 0x00020002, 0x08000000, 0x08021002,
        0x08021000, 0x08000000, 0x00020000, 0x00000002,
        0x08020000, 0x00021002, 0x00001000, 0x08000002,
        0x08001000, 0x08020002, 0x08000002, 0x08001000,
        0x00021000, 0x00000000, 0x00020002, 0x08020000,
        0x00000002, 0x08001002, 0x08021002, 0x00021000],

        [0x20800000, 0x00808020, 0x00000000, 0x20008020,
        0x00800020, 0x00000000, 0x20808000, 0x00800020,
        0x20008000, 0x20000020, 0x20000020, 0x00008000,
        0x20808020, 0x20008000, 0x00008020, 0x20800000,
        0x00000020, 0x20000000, 0x00808020, 0x00800000,
        0x00808000, 0x00008020, 0x20008020, 0x20808000,
        0x20800020, 0x00808000, 0x00008000, 0x20800020,
        0x20000000, 0x20808020, 0x00800000, 0x00000020,
        0x00808020, 0x00000020, 0x20008000, 0x20800000,
        0x00008000, 0x00808020, 0x00800020, 0x00000000,
        0x00800000, 0x20008000, 0x20808020, 0x00800020,
        0x20000020, 0x00800000, 0x00000000, 0x20008020,
        0x20800020, 0x00008000, 0x00000020, 0x20808020,
        0x20000000, 0x20808000, 0x00808000, 0x20000020,
        0x00008020, 0x20800020, 0x20800000, 0x00008020,
        0x20808000, 0x20000000, 0x20008020, 0x00808000],

        [0x00080201, 0x02080001, 0x02080001, 0x02000000,
        0x02080200, 0x02000201, 0x00000201, 0x00080001,
        0x00000000, 0x00080200, 0x00080200, 0x02080201,
        0x02000001, 0x00000000, 0x02000200, 0x00000201,
        0x00000001, 0x00080000, 0x00000200, 0x00080201,
        0x02000000, 0x00000200, 0x00080001, 0x02080000,
        0x02000201, 0x00000001, 0x02080000, 0x02000200,
        0x00080000, 0x02080200, 0x02080201, 0x02000001,
        0x02000200, 0x00000201, 0x00080200, 0x02080201,
        0x02000001, 0x00000000, 0x00000000, 0x00080200,
        0x02080000, 0x02000200, 0x02000201, 0x00000001,
        0x00080201, 0x02080001, 0x02080001, 0x02000000,
        0x02080201, 0x02000001, 0x00000001, 0x00080000,
        0x00000201, 0x00080001, 0x02080200, 0x02000201,
        0x00080001, 0x02080000, 0x00000200, 0x00080201,
        0x02000000, 0x00000200, 0x00080000, 0x02080200],

        [0x01000000, 0x01002080, 0x00002080, 0x01000084,
        0x00002000, 0x01000000, 0x00000004, 0x00002080,
        0x01002004, 0x00002000, 0x01000080, 0x01002004,
        0x01000084, 0x00002084, 0x01002000, 0x00000004,
        0x00000080, 0x00002004, 0x00002004, 0x00000000,
        0x01000004, 0x01002084, 0x01002084, 0x01000080,
        0x00002084, 0x01000004, 0x00000000, 0x00000084,
        0x01002080, 0x00000080, 0x00000084, 0x01002000,
        0x00002000, 0x01000084, 0x01000000, 0x00000080,
        0x00000004, 0x00002080, 0x01000084, 0x01002004,
        0x01000080, 0x00000004, 0x00002084, 0x01002080,
        0x01002004, 0x01000000, 0x00000080, 0x00002084,
        0x01002084, 0x01002000, 0x00000084, 0x01002084,
        0x00002080, 0x00000000, 0x00002004, 0x00000084,
        0x01002000, 0x01000080, 0x01000004, 0x00002000,
        0x00000000, 0x00002004, 0x01002080, 0x01000004],

        [0x10000008, 0x00000408, 0x00040000, 0x10040408,
        0x00000408, 0x10000000, 0x10040408, 0x00000400,
        0x00040008, 0x10040400, 0x00000400, 0x10000008,
        0x10000400, 0x00040008, 0x00000008, 0x10040000,
        0x00000000, 0x10000400, 0x10040008, 0x00040000,
        0x00040400, 0x10040008, 0x10000000, 0x10000408,
        0x10000408, 0x00000000, 0x10040400, 0x00040408,
        0x10040000, 0x00040400, 0x00040408, 0x00000008,
        0x00040008, 0x10000000, 0x10000408, 0x00040400,
        0x10040408, 0x00000400, 0x10040000, 0x10000008,
        0x00000400, 0x00040008, 0x00000008, 0x10040000,
        0x10000008, 0x10040408, 0x00040400, 0x00000408,
        0x10040400, 0x00040408, 0x00000000, 0x10000408,
        0x10000000, 0x00040000, 0x00000408, 0x10040400,
        0x00040000, 0x10000400, 0x10040008, 0x00000000,
        0x00040408, 0x00000008, 0x10000400, 0x10040008],

       [ 0x00000800, 0x80000840, 0x80200040, 0x00000000,
        0x00200000, 0x80200040, 0x80200800, 0x00200840,
        0x80200840, 0x00000800, 0x00000000, 0x80000040,
        0x80000000, 0x00000040, 0x80000840, 0x80200000,
        0x00200040, 0x80200800, 0x80000800, 0x00200040,
        0x80000040, 0x00000840, 0x00200840, 0x80000800,
        0x00000840, 0x00200000, 0x80200000, 0x80200840,
        0x00200800, 0x80000000, 0x00000040, 0x00200800,
        0x00000040, 0x00200800, 0x00000800, 0x80200040,
        0x80200040, 0x80000840, 0x80000840, 0x80000000,
        0x80000800, 0x00000040, 0x00200040, 0x00000800,
        0x00200840, 0x80200000, 0x80200800, 0x00200840,
        0x80200000, 0x80000040, 0x80200840, 0x00000840,
        0x00200800, 0x00000000, 0x80000000, 0x80200840,
        0x00000000, 0x80200800, 0x00000840, 0x00200000,
        0x80000040, 0x00200040, 0x00200000, 0x80000800],

        [0x04100010, 0x00100000, 0x00004000, 0x04104010,
        0x00000010, 0x04100010, 0x04000000, 0x00000010,
        0x04004000, 0x00004010, 0x04104010, 0x00104000,
        0x00104010, 0x04104000, 0x00100000, 0x04000000,
        0x00004010, 0x04000010, 0x00100010, 0x04100000,
        0x00104000, 0x04004000, 0x04004010, 0x00104010,
        0x04100000, 0x00000000, 0x00000000, 0x04004010,
        0x04000010, 0x00100010, 0x04104000, 0x00004000,
        0x04104000, 0x00004000, 0x00104010, 0x00100000,
        0x04000000, 0x04004010, 0x00100000, 0x04104000,
        0x00100010, 0x04000000, 0x04000010, 0x00004010,
        0x04004010, 0x00000010, 0x00004000, 0x04100010,
        0x00000000, 0x04104010, 0x04004000, 0x04000010,
        0x00004010, 0x00100010, 0x04100010, 0x00000000,
        0x04104010, 0x00104000, 0x00104000, 0x04100000,
        0x04100000, 0x04004000, 0x00000010, 0x00104010]
]

# 56 bits of the key are selected from the initial 64 by Permuted Choice 1
def key_choose1(key: str):
    res = ''
    for i in KEY_PC1:
        res += key[i - 1]
    return res

# both halves are rotated left by one or two bits
def key_rotate_left(key: str, n: int):
    return key[n: ] + key[: n]

# 48 subkey bits are selected by Permuted Choice 2
def key_choose2(key: str):
    res = ''
    for i in KEY_PC2:
        res += key[i - 1]
    return res

# the algorithm which generates the subkeys, return the subkeys list
def key_gen(key: int):
    key_list = []
    key_ch1 = key_choose1(bin(key)[2: ].zfill(64))
    key_c = key_ch1[ :28]
    key_d = key_ch1[28: ]
    for i in SHIFT:  
        key_c = key_rotate_left(key_c, i)
        key_d = key_rotate_left(key_d, i)
        key_ch2 = key_choose2(key_c + key_d)
        # print('subkey', i, ':', hex(int(key_ch2, 2)))
        key_list.append(int(key_ch2, 2))
    return key_list


def fp_change(msg_r: int, msg_l: int):
    msg = str(bin(msg_r))[2:].rjust(32, '0') + str(bin(msg_l))[2:].rjust(32, '0')
    res = [0]*64
    for index, i in enumerate(FP):
        res[index] = msg[i - 1]
    return int(''.join(res), 2)

def extend(R):
    out = 0
    out |= R & 1
    out = (out << 5) | ((R >> 27) & 0x1f)
    out = (out << 6) | ((R >> 23) & 0x3f)
    out = (out << 6) | ((R >> 19) & 0x3f)
    out = (out << 6) | ((R >> 15) & 0x3f)
    out = (out << 6) | ((R >> 11) & 0x3f)
    out = (out << 6) | ((R >> 7) & 0x3f)
    out = (out << 6) | ((R >> 3) & 0x3f)
    out = (out << 5) | ( R & 0x1f)
    out = (out << 1) | ((R >> 31) & 1)
    return out


def sp(n):
    ans = 0

    ans = SP_Box[0][n >> 42 & 0x3f] | SP_Box[1][n >> 36 & 0x3f] | SP_Box[2][n >> 30 & 0x3f] | \
          SP_Box[3][n >> 24 & 0x3f] | SP_Box[4][n >> 18 & 0x3f] | SP_Box[5][n >> 12 & 0x3f] | \
          SP_Box[6][n >> 6  & 0x3f] | SP_Box[7][n & 0x3f]

    ans = int((bin(ans)[2:].zfill(32))[::-1], 2)
    return ans

# initial permutation
def initial_permutation(msg: int):
    left = msg >> 32
    right = msg & 0xffffffff
    work = ((left >> 4) ^ right) & 0x0f0f0f0f
    right ^= work
    left ^= (work << 4)
    work = ((left >> 16) ^ right) & 0x0000ffff
    right ^= work
    left ^= (work << 16)
    work = ((right >> 2) ^ left) & 0x33333333
    left ^= work
    right ^= (work << 2)
    work = ((right >> 8) ^ left) & 0x00ff00ff
    left ^= work
    right ^= (work << 8)
    right = ( (right << 1) | ( (right >> 31) & 1) ) & 0xffffffff
    work = (left ^ right) & 0xaaaaaaaa
    left ^= work
    right ^= work
    right = ((right >> 1) | ((right << 31))) & 0xffffffff
    return left, right

# the main process of encryption
def des_encrypt(msg: int, key_list: list, num: int):
    # msg_l: int, msg_r: int
    # msg_l, msg_r = ip_change(msg)
    msg_l, msg_r = initial_permutation(msg)
    
    i = 0
    while i < num:
        # round 1-16
        # f-function

        msg_l, msg_r = msg_r, msg_l ^ sp(extend(msg_r) ^ key_list[0])
        msg_l, msg_r = msg_r, msg_l ^ sp(extend(msg_r) ^ key_list[1])
        msg_l, msg_r = msg_r, msg_l ^ sp(extend(msg_r) ^ key_list[2])
        msg_l, msg_r = msg_r, msg_l ^ sp(extend(msg_r) ^ key_list[3])
        msg_l, msg_r = msg_r, msg_l ^ sp(extend(msg_r) ^ key_list[4])
        msg_l, msg_r = msg_r, msg_l ^ sp(extend(msg_r) ^ key_list[5])   
        msg_l, msg_r = msg_r, msg_l ^ sp(extend(msg_r) ^ key_list[6])
        msg_l, msg_r = msg_r, msg_l ^ sp(extend(msg_r) ^ key_list[7])
        msg_l, msg_r = msg_r, msg_l ^ sp(extend(msg_r) ^ key_list[8])
        msg_l, msg_r = msg_r, msg_l ^ sp(extend(msg_r) ^ key_list[9])
        msg_l, msg_r = msg_r, msg_l ^ sp(extend(msg_r) ^ key_list[10])
        msg_l, msg_r = msg_r, msg_l ^ sp(extend(msg_r) ^ key_list[11]) 
        msg_l, msg_r = msg_r, msg_l ^ sp(extend(msg_r) ^ key_list[12])
        msg_l, msg_r = msg_r, msg_l ^ sp(extend(msg_r) ^ key_list[13])
        msg_l, msg_r = msg_r, msg_l ^ sp(extend(msg_r) ^ key_list[14])
        msg_l, msg_r = msg_r, msg_l ^ sp(extend(msg_r) ^ key_list[15]) 
        msg_l, msg_r = msg_r, msg_l
        i += 1

    ans = fp_change(msg_l, msg_r)
    return ans


def des_encrypt_new(msg: int, key_list: list, num: int):
    # msg_l: int, msg_r: int
    # msg_l, msg_r = ip_change(msg)
    msg_l, msg_r = initial_permutation(msg)
    
    i = 0
    while i < num:
        # round 1-16
        # f-function
        R = msg_r
        etmp = 0
        etmp |= R & 1
        etmp = (etmp << 5) | ((R >> 27) & 0x1f)
        etmp = (etmp << 6) | ((R >> 23) & 0x3f)
        etmp = (etmp << 6) | ((R >> 19) & 0x3f)
        etmp = (etmp << 6) | ((R >> 15) & 0x3f)
        etmp = (etmp << 6) | ((R >> 11) & 0x3f)
        etmp = (etmp << 6) | ((R >> 7) & 0x3f)
        etmp = (etmp << 6) | ((R >> 3) & 0x3f)
        etmp = (etmp << 5) | ( R & 0x1f)
        etmp = (etmp << 1) | ((R >> 31) & 1)
        ktmp = etmp ^ key_list[0]
        sptmp = SP_Box[0][ktmp >> 42 & 0x3f] | SP_Box[1][ktmp >> 36 & 0x3f] | SP_Box[2][ktmp >> 30 & 0x3f] | \
              SP_Box[3][ktmp >> 24 & 0x3f] | SP_Box[4][ktmp >> 18 & 0x3f] | SP_Box[5][ktmp >> 12 & 0x3f] | \
              SP_Box[6][ktmp >> 6  & 0x3f] | SP_Box[7][ktmp & 0x3f]
        sptmp = int((bin(sptmp)[2:].zfill(32))[::-1], 2)
        msg_l, msg_r = msg_r, msg_l ^ sptmp
        
        R = msg_r
        etmp = 0
        etmp |= R & 1
        etmp = (etmp << 5) | ((R >> 27) & 0x1f)
        etmp = (etmp << 6) | ((R >> 23) & 0x3f)
        etmp = (etmp << 6) | ((R >> 19) & 0x3f)
        etmp = (etmp << 6) | ((R >> 15) & 0x3f)
        etmp = (etmp << 6) | ((R >> 11) & 0x3f)
        etmp = (etmp << 6) | ((R >> 7) & 0x3f)
        etmp = (etmp << 6) | ((R >> 3) & 0x3f)
        etmp = (etmp << 5) | ( R & 0x1f)
        etmp = (etmp << 1) | ((R >> 31) & 1)
        ktmp = etmp ^ key_list[1]
        sptmp = SP_Box[0][ktmp >> 42 & 0x3f] | SP_Box[1][ktmp >> 36 & 0x3f] | SP_Box[2][ktmp >> 30 & 0x3f] | \
              SP_Box[3][ktmp >> 24 & 0x3f] | SP_Box[4][ktmp >> 18 & 0x3f] | SP_Box[5][ktmp >> 12 & 0x3f] | \
              SP_Box[6][ktmp >> 6  & 0x3f] | SP_Box[7][ktmp & 0x3f]
        sptmp = int((bin(sptmp)[2:].zfill(32))[::-1], 2)
        msg_l, msg_r = msg_r, msg_l ^ sptmp

        R = msg_r
        etmp = 0
        etmp |= R & 1
        etmp = (etmp << 5) | ((R >> 27) & 0x1f)
        etmp = (etmp << 6) | ((R >> 23) & 0x3f)
        etmp = (etmp << 6) | ((R >> 19) & 0x3f)
        etmp = (etmp << 6) | ((R >> 15) & 0x3f)
        etmp = (etmp << 6) | ((R >> 11) & 0x3f)
        etmp = (etmp << 6) | ((R >> 7) & 0x3f)
        etmp = (etmp << 6) | ((R >> 3) & 0x3f)
        etmp = (etmp << 5) | ( R & 0x1f)
        etmp = (etmp << 1) | ((R >> 31) & 1)
        ktmp = etmp ^ key_list[2]
        sptmp = SP_Box[0][ktmp >> 42 & 0x3f] | SP_Box[1][ktmp >> 36 & 0x3f] | SP_Box[2][ktmp >> 30 & 0x3f] | \
              SP_Box[3][ktmp >> 24 & 0x3f] | SP_Box[4][ktmp >> 18 & 0x3f] | SP_Box[5][ktmp >> 12 & 0x3f] | \
              SP_Box[6][ktmp >> 6  & 0x3f] | SP_Box[7][ktmp & 0x3f]
        sptmp = int((bin(sptmp)[2:].zfill(32))[::-1], 2)
        msg_l, msg_r = msg_r, msg_l ^ sptmp

        R = msg_r
        etmp = 0
        etmp |= R & 1
        etmp = (etmp << 5) | ((R >> 27) & 0x1f)
        etmp = (etmp << 6) | ((R >> 23) & 0x3f)
        etmp = (etmp << 6) | ((R >> 19) & 0x3f)
        etmp = (etmp << 6) | ((R >> 15) & 0x3f)
        etmp = (etmp << 6) | ((R >> 11) & 0x3f)
        etmp = (etmp << 6) | ((R >> 7) & 0x3f)
        etmp = (etmp << 6) | ((R >> 3) & 0x3f)
        etmp = (etmp << 5) | ( R & 0x1f)
        etmp = (etmp << 1) | ((R >> 31) & 1)
        ktmp = etmp ^ key_list[3]
        sptmp = SP_Box[0][ktmp >> 42 & 0x3f] | SP_Box[1][ktmp >> 36 & 0x3f] | SP_Box[2][ktmp >> 30 & 0x3f] | \
              SP_Box[3][ktmp >> 24 & 0x3f] | SP_Box[4][ktmp >> 18 & 0x3f] | SP_Box[5][ktmp >> 12 & 0x3f] | \
              SP_Box[6][ktmp >> 6  & 0x3f] | SP_Box[7][ktmp & 0x3f]
        sptmp = int((bin(sptmp)[2:].zfill(32))[::-1], 2)
        msg_l, msg_r = msg_r, msg_l ^ sptmp

        R = msg_r
        etmp = 0
        etmp |= R & 1
        etmp = (etmp << 5) | ((R >> 27) & 0x1f)
        etmp = (etmp << 6) | ((R >> 23) & 0x3f)
        etmp = (etmp << 6) | ((R >> 19) & 0x3f)
        etmp = (etmp << 6) | ((R >> 15) & 0x3f)
        etmp = (etmp << 6) | ((R >> 11) & 0x3f)
        etmp = (etmp << 6) | ((R >> 7) & 0x3f)
        etmp = (etmp << 6) | ((R >> 3) & 0x3f)
        etmp = (etmp << 5) | ( R & 0x1f)
        etmp = (etmp << 1) | ((R >> 31) & 1)
        ktmp = etmp ^ key_list[4]
        sptmp = SP_Box[0][ktmp >> 42 & 0x3f] | SP_Box[1][ktmp >> 36 & 0x3f] | SP_Box[2][ktmp >> 30 & 0x3f] | \
              SP_Box[3][ktmp >> 24 & 0x3f] | SP_Box[4][ktmp >> 18 & 0x3f] | SP_Box[5][ktmp >> 12 & 0x3f] | \
              SP_Box[6][ktmp >> 6  & 0x3f] | SP_Box[7][ktmp & 0x3f]
        sptmp = int((bin(sptmp)[2:].zfill(32))[::-1], 2)
        msg_l, msg_r = msg_r, msg_l ^ sptmp

        R = msg_r
        etmp = 0
        etmp |= R & 1
        etmp = (etmp << 5) | ((R >> 27) & 0x1f)
        etmp = (etmp << 6) | ((R >> 23) & 0x3f)
        etmp = (etmp << 6) | ((R >> 19) & 0x3f)
        etmp = (etmp << 6) | ((R >> 15) & 0x3f)
        etmp = (etmp << 6) | ((R >> 11) & 0x3f)
        etmp = (etmp << 6) | ((R >> 7) & 0x3f)
        etmp = (etmp << 6) | ((R >> 3) & 0x3f)
        etmp = (etmp << 5) | ( R & 0x1f)
        etmp = (etmp << 1) | ((R >> 31) & 1)
        ktmp = etmp ^ key_list[5]
        sptmp = SP_Box[0][ktmp >> 42 & 0x3f] | SP_Box[1][ktmp >> 36 & 0x3f] | SP_Box[2][ktmp >> 30 & 0x3f] | \
              SP_Box[3][ktmp >> 24 & 0x3f] | SP_Box[4][ktmp >> 18 & 0x3f] | SP_Box[5][ktmp >> 12 & 0x3f] | \
              SP_Box[6][ktmp >> 6  & 0x3f] | SP_Box[7][ktmp & 0x3f]
        sptmp = int((bin(sptmp)[2:].zfill(32))[::-1], 2)
        msg_l, msg_r = msg_r, msg_l ^ sptmp

        R = msg_r
        etmp = 0
        etmp |= R & 1
        etmp = (etmp << 5) | ((R >> 27) & 0x1f)
        etmp = (etmp << 6) | ((R >> 23) & 0x3f)
        etmp = (etmp << 6) | ((R >> 19) & 0x3f)
        etmp = (etmp << 6) | ((R >> 15) & 0x3f)
        etmp = (etmp << 6) | ((R >> 11) & 0x3f)
        etmp = (etmp << 6) | ((R >> 7) & 0x3f)
        etmp = (etmp << 6) | ((R >> 3) & 0x3f)
        etmp = (etmp << 5) | ( R & 0x1f)
        etmp = (etmp << 1) | ((R >> 31) & 1)
        ktmp = etmp ^ key_list[6]
        sptmp = SP_Box[0][ktmp >> 42 & 0x3f] | SP_Box[1][ktmp >> 36 & 0x3f] | SP_Box[2][ktmp >> 30 & 0x3f] | \
              SP_Box[3][ktmp >> 24 & 0x3f] | SP_Box[4][ktmp >> 18 & 0x3f] | SP_Box[5][ktmp >> 12 & 0x3f] | \
              SP_Box[6][ktmp >> 6  & 0x3f] | SP_Box[7][ktmp & 0x3f]
        sptmp = int((bin(sptmp)[2:].zfill(32))[::-1], 2)
        msg_l, msg_r = msg_r, msg_l ^ sptmp

        R = msg_r
        etmp = 0
        etmp |= R & 1
        etmp = (etmp << 5) | ((R >> 27) & 0x1f)
        etmp = (etmp << 6) | ((R >> 23) & 0x3f)
        etmp = (etmp << 6) | ((R >> 19) & 0x3f)
        etmp = (etmp << 6) | ((R >> 15) & 0x3f)
        etmp = (etmp << 6) | ((R >> 11) & 0x3f)
        etmp = (etmp << 6) | ((R >> 7) & 0x3f)
        etmp = (etmp << 6) | ((R >> 3) & 0x3f)
        etmp = (etmp << 5) | ( R & 0x1f)
        etmp = (etmp << 1) | ((R >> 31) & 1)
        ktmp = etmp ^ key_list[7]
        sptmp = SP_Box[0][ktmp >> 42 & 0x3f] | SP_Box[1][ktmp >> 36 & 0x3f] | SP_Box[2][ktmp >> 30 & 0x3f] | \
              SP_Box[3][ktmp >> 24 & 0x3f] | SP_Box[4][ktmp >> 18 & 0x3f] | SP_Box[5][ktmp >> 12 & 0x3f] | \
              SP_Box[6][ktmp >> 6  & 0x3f] | SP_Box[7][ktmp & 0x3f]
        sptmp = int((bin(sptmp)[2:].zfill(32))[::-1], 2)
        msg_l, msg_r = msg_r, msg_l ^ sptmp

        R = msg_r
        etmp = 0
        etmp |= R & 1
        etmp = (etmp << 5) | ((R >> 27) & 0x1f)
        etmp = (etmp << 6) | ((R >> 23) & 0x3f)
        etmp = (etmp << 6) | ((R >> 19) & 0x3f)
        etmp = (etmp << 6) | ((R >> 15) & 0x3f)
        etmp = (etmp << 6) | ((R >> 11) & 0x3f)
        etmp = (etmp << 6) | ((R >> 7) & 0x3f)
        etmp = (etmp << 6) | ((R >> 3) & 0x3f)
        etmp = (etmp << 5) | ( R & 0x1f)
        etmp = (etmp << 1) | ((R >> 31) & 1)
        ktmp = etmp ^ key_list[8]
        sptmp = SP_Box[0][ktmp >> 42 & 0x3f] | SP_Box[1][ktmp >> 36 & 0x3f] | SP_Box[2][ktmp >> 30 & 0x3f] | \
              SP_Box[3][ktmp >> 24 & 0x3f] | SP_Box[4][ktmp >> 18 & 0x3f] | SP_Box[5][ktmp >> 12 & 0x3f] | \
              SP_Box[6][ktmp >> 6  & 0x3f] | SP_Box[7][ktmp & 0x3f]
        sptmp = int((bin(sptmp)[2:].zfill(32))[::-1], 2)
        msg_l, msg_r = msg_r, msg_l ^ sptmp

        R = msg_r
        etmp = 0
        etmp |= R & 1
        etmp = (etmp << 5) | ((R >> 27) & 0x1f)
        etmp = (etmp << 6) | ((R >> 23) & 0x3f)
        etmp = (etmp << 6) | ((R >> 19) & 0x3f)
        etmp = (etmp << 6) | ((R >> 15) & 0x3f)
        etmp = (etmp << 6) | ((R >> 11) & 0x3f)
        etmp = (etmp << 6) | ((R >> 7) & 0x3f)
        etmp = (etmp << 6) | ((R >> 3) & 0x3f)
        etmp = (etmp << 5) | ( R & 0x1f)
        etmp = (etmp << 1) | ((R >> 31) & 1)
        ktmp = etmp ^ key_list[9]
        sptmp = SP_Box[0][ktmp >> 42 & 0x3f] | SP_Box[1][ktmp >> 36 & 0x3f] | SP_Box[2][ktmp >> 30 & 0x3f] | \
              SP_Box[3][ktmp >> 24 & 0x3f] | SP_Box[4][ktmp >> 18 & 0x3f] | SP_Box[5][ktmp >> 12 & 0x3f] | \
              SP_Box[6][ktmp >> 6  & 0x3f] | SP_Box[7][ktmp & 0x3f]
        sptmp = int((bin(sptmp)[2:].zfill(32))[::-1], 2)
        msg_l, msg_r = msg_r, msg_l ^ sptmp

        R = msg_r
        etmp = 0
        etmp |= R & 1
        etmp = (etmp << 5) | ((R >> 27) & 0x1f)
        etmp = (etmp << 6) | ((R >> 23) & 0x3f)
        etmp = (etmp << 6) | ((R >> 19) & 0x3f)
        etmp = (etmp << 6) | ((R >> 15) & 0x3f)
        etmp = (etmp << 6) | ((R >> 11) & 0x3f)
        etmp = (etmp << 6) | ((R >> 7) & 0x3f)
        etmp = (etmp << 6) | ((R >> 3) & 0x3f)
        etmp = (etmp << 5) | ( R & 0x1f)
        etmp = (etmp << 1) | ((R >> 31) & 1)
        ktmp = etmp ^ key_list[10]
        sptmp = SP_Box[0][ktmp >> 42 & 0x3f] | SP_Box[1][ktmp >> 36 & 0x3f] | SP_Box[2][ktmp >> 30 & 0x3f] | \
              SP_Box[3][ktmp >> 24 & 0x3f] | SP_Box[4][ktmp >> 18 & 0x3f] | SP_Box[5][ktmp >> 12 & 0x3f] | \
              SP_Box[6][ktmp >> 6  & 0x3f] | SP_Box[7][ktmp & 0x3f]
        sptmp = int((bin(sptmp)[2:].zfill(32))[::-1], 2)
        msg_l, msg_r = msg_r, msg_l ^ sptmp

        R = msg_r
        etmp = 0
        etmp |= R & 1
        etmp = (etmp << 5) | ((R >> 27) & 0x1f)
        etmp = (etmp << 6) | ((R >> 23) & 0x3f)
        etmp = (etmp << 6) | ((R >> 19) & 0x3f)
        etmp = (etmp << 6) | ((R >> 15) & 0x3f)
        etmp = (etmp << 6) | ((R >> 11) & 0x3f)
        etmp = (etmp << 6) | ((R >> 7) & 0x3f)
        etmp = (etmp << 6) | ((R >> 3) & 0x3f)
        etmp = (etmp << 5) | ( R & 0x1f)
        etmp = (etmp << 1) | ((R >> 31) & 1)
        ktmp = etmp ^ key_list[11]
        sptmp = SP_Box[0][ktmp >> 42 & 0x3f] | SP_Box[1][ktmp >> 36 & 0x3f] | SP_Box[2][ktmp >> 30 & 0x3f] | \
              SP_Box[3][ktmp >> 24 & 0x3f] | SP_Box[4][ktmp >> 18 & 0x3f] | SP_Box[5][ktmp >> 12 & 0x3f] | \
              SP_Box[6][ktmp >> 6  & 0x3f] | SP_Box[7][ktmp & 0x3f]
        sptmp = int((bin(sptmp)[2:].zfill(32))[::-1], 2)
        msg_l, msg_r = msg_r, msg_l ^ sptmp

        R = msg_r
        etmp = 0
        etmp |= R & 1
        etmp = (etmp << 5) | ((R >> 27) & 0x1f)
        etmp = (etmp << 6) | ((R >> 23) & 0x3f)
        etmp = (etmp << 6) | ((R >> 19) & 0x3f)
        etmp = (etmp << 6) | ((R >> 15) & 0x3f)
        etmp = (etmp << 6) | ((R >> 11) & 0x3f)
        etmp = (etmp << 6) | ((R >> 7) & 0x3f)
        etmp = (etmp << 6) | ((R >> 3) & 0x3f)
        etmp = (etmp << 5) | ( R & 0x1f)
        etmp = (etmp << 1) | ((R >> 31) & 1)
        ktmp = etmp ^ key_list[12]
        sptmp = SP_Box[0][ktmp >> 42 & 0x3f] | SP_Box[1][ktmp >> 36 & 0x3f] | SP_Box[2][ktmp >> 30 & 0x3f] | \
              SP_Box[3][ktmp >> 24 & 0x3f] | SP_Box[4][ktmp >> 18 & 0x3f] | SP_Box[5][ktmp >> 12 & 0x3f] | \
              SP_Box[6][ktmp >> 6  & 0x3f] | SP_Box[7][ktmp & 0x3f]
        sptmp = int((bin(sptmp)[2:].zfill(32))[::-1], 2)
        msg_l, msg_r = msg_r, msg_l ^ sptmp

        R = msg_r
        etmp = 0
        etmp |= R & 1
        etmp = (etmp << 5) | ((R >> 27) & 0x1f)
        etmp = (etmp << 6) | ((R >> 23) & 0x3f)
        etmp = (etmp << 6) | ((R >> 19) & 0x3f)
        etmp = (etmp << 6) | ((R >> 15) & 0x3f)
        etmp = (etmp << 6) | ((R >> 11) & 0x3f)
        etmp = (etmp << 6) | ((R >> 7) & 0x3f)
        etmp = (etmp << 6) | ((R >> 3) & 0x3f)
        etmp = (etmp << 5) | ( R & 0x1f)
        etmp = (etmp << 1) | ((R >> 31) & 1)
        ktmp = etmp ^ key_list[13]
        sptmp = SP_Box[0][ktmp >> 42 & 0x3f] | SP_Box[1][ktmp >> 36 & 0x3f] | SP_Box[2][ktmp >> 30 & 0x3f] | \
              SP_Box[3][ktmp >> 24 & 0x3f] | SP_Box[4][ktmp >> 18 & 0x3f] | SP_Box[5][ktmp >> 12 & 0x3f] | \
              SP_Box[6][ktmp >> 6  & 0x3f] | SP_Box[7][ktmp & 0x3f]
        sptmp = int((bin(sptmp)[2:].zfill(32))[::-1], 2)
        msg_l, msg_r = msg_r, msg_l ^ sptmp

        R = msg_r
        etmp = 0
        etmp |= R & 1
        etmp = (etmp << 5) | ((R >> 27) & 0x1f)
        etmp = (etmp << 6) | ((R >> 23) & 0x3f)
        etmp = (etmp << 6) | ((R >> 19) & 0x3f)
        etmp = (etmp << 6) | ((R >> 15) & 0x3f)
        etmp = (etmp << 6) | ((R >> 11) & 0x3f)
        etmp = (etmp << 6) | ((R >> 7) & 0x3f)
        etmp = (etmp << 6) | ((R >> 3) & 0x3f)
        etmp = (etmp << 5) | ( R & 0x1f)
        etmp = (etmp << 1) | ((R >> 31) & 1)
        ktmp = etmp ^ key_list[14]
        sptmp = SP_Box[0][ktmp >> 42 & 0x3f] | SP_Box[1][ktmp >> 36 & 0x3f] | SP_Box[2][ktmp >> 30 & 0x3f] | \
              SP_Box[3][ktmp >> 24 & 0x3f] | SP_Box[4][ktmp >> 18 & 0x3f] | SP_Box[5][ktmp >> 12 & 0x3f] | \
              SP_Box[6][ktmp >> 6  & 0x3f] | SP_Box[7][ktmp & 0x3f]
        sptmp = int((bin(sptmp)[2:].zfill(32))[::-1], 2)
        msg_l, msg_r = msg_r, msg_l ^ sptmp

        R = msg_r
        etmp = 0
        etmp |= R & 1
        etmp = (etmp << 5) | ((R >> 27) & 0x1f)
        etmp = (etmp << 6) | ((R >> 23) & 0x3f)
        etmp = (etmp << 6) | ((R >> 19) & 0x3f)
        etmp = (etmp << 6) | ((R >> 15) & 0x3f)
        etmp = (etmp << 6) | ((R >> 11) & 0x3f)
        etmp = (etmp << 6) | ((R >> 7) & 0x3f)
        etmp = (etmp << 6) | ((R >> 3) & 0x3f)
        etmp = (etmp << 5) | ( R & 0x1f)
        etmp = (etmp << 1) | ((R >> 31) & 1)
        ktmp = etmp ^ key_list[15]
        sptmp = SP_Box[0][ktmp >> 42 & 0x3f] | SP_Box[1][ktmp >> 36 & 0x3f] | SP_Box[2][ktmp >> 30 & 0x3f] | \
              SP_Box[3][ktmp >> 24 & 0x3f] | SP_Box[4][ktmp >> 18 & 0x3f] | SP_Box[5][ktmp >> 12 & 0x3f] | \
              SP_Box[6][ktmp >> 6  & 0x3f] | SP_Box[7][ktmp & 0x3f]
        sptmp = int((bin(sptmp)[2:].zfill(32))[::-1], 2)
        msg_l, msg_r = msg_r, msg_l ^ sptmp


        msg_l, msg_r = msg_r, msg_l
        i += 1

    ans = fp_change(msg_l, msg_r)
    return ans



def test_fastDES(msg, key, num):
    import time
    start = time.time()
    key_list = key_gen(key)
    ans = des_encrypt_new(msg, key_list, num)
    end = time.time()
    return ans, end - start


if __name__ == '__main__':
    num = int(input())
    msg = int(input(), 16)
    key = int(input(), 16)

    key_list = key_gen(key)

    ans = des_encrypt(msg, key_list, num)

    print('0x' + hex(ans)[2:].rjust(16, '0'))

    
