KEY_PC1 =  [57, 49, 41, 33, 25, 17,  9,  1, 58, 50, 42, 34, 26, 18,
            10,  2, 59, 51, 43, 35, 27, 19, 11,  3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,  7, 62, 54, 46, 38, 30, 22,
            14,  6, 61, 53, 45, 37, 29, 21, 13,  5, 28, 20, 12,  4]
KEY_PC2 =  [14, 17, 11, 24,  1,  5,  3, 28, 15,  6, 21, 10,
            23, 19, 12,  4, 26,  8, 16,  7, 27, 20, 13,  2,
            41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
SHIFT =    [ 1,  1,  2,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  2,  1]
IP =       [58, 50, 42, 34, 26, 18, 10,  2, 60, 52, 44, 36, 28, 20, 12,  4,
            62, 54, 46, 38, 30, 22, 14,  6, 64, 56, 48, 40, 32, 24, 16,  8,
            57, 49, 41, 33, 25, 17,  9,  1, 59, 51, 43, 35, 27, 19, 11,  3,
            61, 53, 45, 37, 29, 21, 13,  5, 63, 55, 47, 39, 31, 23, 15,  7]
FP =       [40,  8, 48, 16, 56, 24, 64, 32, 39,  7, 47, 15, 55, 23, 63, 31,
            38,  6, 46, 14, 54, 22, 62, 30, 37,  5, 45, 13, 53, 21, 61, 29,
            36,  4, 44, 12, 52, 20, 60, 28, 35,  3, 43, 11, 51, 19, 59, 27,
            34,  2, 42, 10, 50, 18, 58, 26, 33,  1, 41,  9, 49, 17, 57, 25]
E  =       [32,  1,  2,  3,  4,  5,  4,  5,
             6,  7,  8,  9,  8,  9, 10, 11,
            12, 13, 12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21, 20, 21,
            22, 23, 24, 25, 24, 25, 26, 27,
            28, 29, 28, 29, 30, 31, 32,  1]
P = [16,  7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26,  5, 18, 31, 10,
     2,  8, 24, 14, 32, 27,  3,  9,
     19, 13, 30, 6, 22, 11,  4,  25]
S =  [
[14, 4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
     4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
     15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13 ],
[15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
     3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
     0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
     13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9],
[10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
     13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
     13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
     1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12 ],
[7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11,  12,  4, 15,
     13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,9,
     10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
     3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14],
[2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
     14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
     4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
     11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3],
[12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
     10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
     9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
     4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13],
[4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
     13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
     1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
     6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12],
[13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
     1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
     7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
     2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11],
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
def key_gen(key: str):
    key_list = []
    key_ch1 = key_choose1(key)
    key_c = key_ch1[ :28]
    key_d = key_ch1[28: ]
    for i in SHIFT:  
        key_c = key_rotate_left(key_c, i)
        key_d = key_rotate_left(key_d, i)
        key_ch2 = key_choose2(key_c + key_d)
        # print('subkey', i, ':', hex(int(key_ch2, 2)))
        key_list.append(key_ch2)
    return key_list

# initial and final permutation which are inverses
def ip_change(msg: str):
    res = ''
    for i in IP:
        res += msg[i - 1]
    return res[ :32], res[32: ]

def fp_change(msg: str):
    res = ''
    for i in FP:
        res += msg[i - 1]
    return res

# exclusive xor operation on two 01 strings of string type
def xor_cal(a: str, b: str):
    if len(a) != len(b):
        raise Exception('the two strings are not the same length!')
    res = ''
    for i in range(len(a)):
        res += str(int(a[i]) ^ int(b[i])).ljust(1, '0')
    return res


# f-function consists of four stages
def f_function(msg: str, key: str, i: int):
    msg_e = e_expansion(msg)
    msg_k = xor_cal(msg_e, key)
    msg_s = s_substitution(msg_k)
    msg_p = p_permutation(msg_s)
    # print(i, hex(int(msg_e,2)), hex(int(msg_k,2)), hex(int(msg_s,2)), hex(int(msg_p,2)))
    return msg_p

# the 32-bit half-block is expanded to 48 bits using the expansion permutation
def e_expansion(msg: str):
    res = ''
    for i in E:
        res += msg[i - 1]
    return res

# the block is divided into eight 6-bit pieces before processing by the S-boxes
def s_substitution(msg: str):
    res = ''
    msg_slice = [msg[i:i+6] for i in range(0, len(msg), 6)]
    for i, sl in enumerate(msg_slice):
        row    = int(sl[0]+sl[5], 2)
        column = int(sl[1:5],     2)
        num = row * 16 + column
        res += bin(S[i][num])[2: ].rjust(4, '0')
        # print(i, sl, int(sl, 2), bin(S[i][num])[2: ].rjust(4, '0'), int(bin(S[i][num])[2: ].rjust(4, '0'), 2))
        
    return res

# the 32 outputs from the S-boxes are rearranged according to a fixed permutation
def p_permutation(msg: str):
    res = ''
    for i in P:
        res += msg[i - 1]
    return res

# the main process of encryption
def des_encrypt(msg: str, key: str):
    key_list = key_gen(key)
    msg_l, msg_r = ip_change(msg)
    # print('msg_l0:', hex(int(msg_l, 2)), 'msg_r0:', hex(int(msg_r, 2)))
    # print('msg_l', 0, ':', hex(int(msg_l, 2)), 'msg_r', 0, ':', hex(int(msg_r, 2)))
    for i in range(16):
        tmp_l = msg_r
        tmp_r = xor_cal(msg_l, f_function(msg_r, key_list[i], i))
        msg_l, msg_r = tmp_l, tmp_r
        # print('msg_l', i+1, ':', hex(int(msg_l, 2)), 'msg_r', i+1, ':', hex(int(msg_r, 2)))
    ans = fp_change(msg_r + msg_l)
    return ans

# the main process of decryption
def des_decrypt(cip: str, key: str):
    key_list = key_gen(key)[::-1]
    cip_l, cip_r = ip_change(cip)
    for i in range(16):
        tmp_l = cip_r
        tmp_r = xor_cal(cip_l, f_function(cip_r, key_list[i], i))
        cip_l, cip_r = tmp_l, tmp_r
    ans = fp_change(cip_r + cip_l)
    return ans

def input_value():
    num = int(input())
    msg = input().strip()
    key = input().strip()
    mode = 1
    msg_bin = bin(int(msg, 16))[2: ].rjust(64, '0')
    key_bin = bin(int(key, 16))[2: ].rjust(64, '0')  
    return msg_bin, key_bin, num, mode

def test_normalDES(msg, key, num):
    msg = bin(int(msg, 16))[2: ].rjust(64, '0')
    key = bin(int(key, 16))[2: ].rjust(64, '0')
    import time
    start = time.time()
    for _ in range(num):
        ans = des_encrypt(msg, key)
        msg = ans
    end = time.time()
    return int(ans, 2), end - start

if __name__ == '__main__':
    import time
    msg, key, num, mode = input_value()
    start = time.time()
    for _ in range(num):
        if mode == 1:
            ans = des_encrypt(msg, key)
        elif mode == 0:
            ans = des_decrypt(msg, key)
        msg = ans
    end = time.time()
    print('time:', end - start)
    print('0x' + hex(int(ans, 2))[2:].rjust(16, '0'))
