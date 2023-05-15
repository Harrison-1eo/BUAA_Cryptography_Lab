def inputValue():
    s = input()
    a = int(s[0], 16)
    return a

def GF_plus(a, b):
    return a ^ b

def GF_sub(a, b):
    return GF_plus(a, b)

def GF_multi(a, b, mod=0x11b):
    ans = 0
    while b > 0:
        if str(bin(b))[-1] == '1':
            ans = GF_plus(ans, a)
        a = a << 1
        if a.bit_length() > 8 :
            a = GF_sub(a, mod)
        a = a & 0xff
        b = b >> 1
    return ans

def GF_div(a, b):
    ans = 0
    al = a.bit_length()
    bl = b.bit_length() 
    dl = al - bl
    if dl < 0:
        return 0, a
    elif dl == 0:
        return 1, a ^ b
    else:
        while al >= bl:
            rec = al - bl
            a   ^= (b << rec)
            ans |= (1 << rec)
            al = a.bit_length()
        return ans, a

def GF_exgcd(a, b):
    if b == 0:
        return 1, 0, a
    x_, y_, gcd = GF_exgcd(b, GF_div(a, b)[1])
    ppx = y_
    ppy = x_ ^ GF_multi(y_, GF_div(a, b)[0])
    return ppx, ppy, gcd

a = inputValue()
x,y,gcd = GF_exgcd(a, 0x11b)
print(hex(x)[2:].rjust(2, '0'))
# print(x, y, gcd)

