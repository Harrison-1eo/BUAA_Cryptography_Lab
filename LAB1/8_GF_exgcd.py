def inputValue():
    s = input().split(' ')
    a = int(s[0], 16)
    b = int(s[1], 16)
    return a, b

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
    a_l = a.bit_length()
    b_l = b.bit_length() 
    while a_l >= b_l:
        rec = a_l - b_l
        a   ^= (b << rec)
        ans |= (1 << rec)
        a_l = a.bit_length()
    return ans, a

def GF_exgcd(a, b):
    r, s, t = a, 1, 0
    r_, s_, t_ = b, 0, 1
    while r_ != 0:
        q, _ = GF_div(r, r_)
        temp1 = r ^ GF_multi(q, r_)
        temp2 = s ^ GF_multi(q, s_)
        temp3 = t ^ GF_multi(q, t_)
        r, s, t = r_, s_, t_
        r_, s_, t_ = temp1, temp2, temp3
    ppx, ppy, gcd = s, t, r
    #if gcd < 0:
    #    ppx, ppy, gcd = -ppx, -ppy, -gcd
    assert GF_multi(ppx, a) ^ GF_multi(ppy, b) == gcd
    # print(ppx ,a, ppy, b, gcd)
    return ppx, ppy, gcd

def GF_pow(a, b, mod=0x11b):
    for _ in range(b):
        a = GF_multi(a, a, mod)
    return a


a, b = inputValue()
x, y, g = GF_exgcd(a, b)
print(hex(x)[2:].rjust(2, '0'), hex(y)[2:].rjust(2, '0'), hex(g)[2:].rjust(2, '0'), sep=' ')