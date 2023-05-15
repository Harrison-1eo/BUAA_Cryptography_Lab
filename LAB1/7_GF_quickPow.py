def inputValue():
    s = input().split(' ')
    a = int(s[0], 16)
    b = int(s[1], 10)
    return a, b

def GF_plus(a, b):
    return a ^ b

def GF_sub(a, b):
    return GF_plus(a, b)

def GF_multi(a, b):
    ans = 0
    while b > 0:
        if str(bin(b))[-1] == '1':
            ans = GF_plus(ans, a)
        a = a << 1
        if len(str(bin(a))[2:]) > 8 :
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
        while len(str(bin(ans))[2:]) > 8 :
            ans = GF_sub(ans, 0x11b)
        ans &= 0xff
    return ans 

a, b = inputValue()
print(hex(GF_quickPow(a, b))[2:].rjust(2, '0'))
