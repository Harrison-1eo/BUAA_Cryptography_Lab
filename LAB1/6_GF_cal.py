def inputValue():
    s = input().split(' ')
    a = int(s[0], 16)
    b = int(s[2], 16)
    return a, b, s[1]

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

def GF_div(a, b):
    ans = 0
    while len(bin(a)) >= len(bin(b)):
        rec = len(bin(a)) - len(bin(b))
        a ^= (b << rec)
        ans ^= (1 << rec)
    #return ans, a
    return hex(ans)[2:].rjust(2, '0')+' '+hex(a)[2:].rjust(2, '0')

a, b, cal = inputValue()
if cal == '+':
    print(hex(GF_plus(a, b))[2:].rjust(2, '0'))
elif cal == '-':
    print(hex(GF_sub(a, b))[2:].rjust(2, '0'))
elif cal == '*':
    print(hex(GF_multi(a, b))[2:].rjust(2, '0'))
elif cal == '/':
    print(GF_div(a, b))
else:
    print('op error')