def GF_plus(a, b):
    return a ^ b


def GF_sub(a, b):
    return a ^ b


def GF_multi(a, b):
    ans = 0
    while b > 0:
        if str(bin(b))[-1] == '1':
            ans = GF_plus(ans, a)
        a = a << 1
        if len(str(bin(a))[2:]) > 8:
            a = GF_sub(a, 0x11b)
        a = a & 0xff
        b = b >> 1
    return ans


def GF_quickPow(a, b):
    ans = 1
    binary = str(bin(b))[2:]
    for i in binary:
        ans = GF_multi(ans, ans)
        if i == '1':
            ans = GF_multi(ans, a)
        while len(str(bin(ans))[2:]) > 8:
            ans = GF_sub(ans, 0x11b)
        ans &= 0xff
    return ans

# a: int, return: int
def GF_inverse(a):
    b = 2 ** 8 - 2
    return GF_quickPow(a, b)


def bitChange(a, mode):
    bit = bin(a)[2:].rjust(8, '0')
    bit = bit[::-1]
    c = list('01100011')[::-1] if mode == 1 else list('01100011')
    ans = [0 for i in range(8)]
    for i in range(8):
        ans[i] = int(bit[i]) ^ int(bit[(i+4) % 8]) ^ int(bit[(i+5) % 8]) ^ int(bit[(i+6) % 8]) ^ int(bit[(i+7) % 8]) ^ int(c[i])
    ans = ans[::-1]
    return int(''.join([str(i) for i in ans]), 2)


def SBOX_print(SBOX):
    for i in range(16):
        print('[', end='')
        for j in range(16):
            if j == 15:
                print('0x'+hex(SBOX[i][j])[2:].rjust(2, '0'), end='')
            else:
                print('0x'+hex(SBOX[i][j])[2:].rjust(2, '0'), end=', ')
        print('],')
    print()


def SBOX_generate():
    SBOX = [[(j*16+i) for i in range(16)] for j in range(16)]
    SBOX_print(SBOX)

    for i in range(16):
        for j in range(16):
            SBOX[i][j] = GF_inverse(SBOX[i][j])
    SBOX_print(SBOX)

    for i in range(16):
        for j in range(16):
            SBOX[i][j] = bitChange(SBOX[i][j], 1)
    SBOX_print(SBOX)
    return SBOX


def SBOX_inverse(SBOX):
    S = []
    for i in range(16):
        for j in range(16):
            S.append(SBOX[i][j])
    SBOX_inv = [[0 for i in range(16)] for j in range(16)]
    for i in range(256):
        SBOX_inv[i//16][i % 16] = S.index(i)
    SBOX_print(SBOX_inv)


if '__main__' == __name__:
    SBOX = SBOX_generate()
    SBOX_inverse(SBOX)
