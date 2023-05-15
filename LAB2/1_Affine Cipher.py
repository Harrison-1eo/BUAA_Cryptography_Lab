def gcd(x, y):
    while y:
        t = x % y
        x = y
        y = t 
    return x

def exgcd(a, b):
    r, s, t = a, 1, 0
    r_, s_, t_ = b, 0, 1
    while r_ != 0:
        q = r//r_
        temp1 = r-q*r_
        temp2 = s-q*s_
        temp3 = t-q*t_
        r, s, t = r_, s_, t_
        r_, s_, t_ = temp1, temp2, temp3
    ppx, ppy, gcd = s, t, r
    if r < 0:
        ppx, ppy, gcd = -ppx, -ppy, -gcd
    assert ppx * a + ppy * b == gcd
    while ppx <= 0:
        if b < 0:
            ppx -= b // gcd
            ppy += a // gcd
        else:
            ppx += b // gcd
            ppy -= a // gcd
    # print(ppx ,a, ppy, b, gcd)
    return ppx, ppy, gcd

def inputValue():
    s = input().split(' ')
    a = int(s[0])
    b = int(s[1])
    c = input().strip()
    d = int(input())
    return a, b, c, d

def checkKey(k):
    if gcd(k, 26) != 1:
        return True
    else:
        return False

def encode(k:int, b:int, msg:str):
    ans = ''
    for i in msg:
        a = ((ord(i) - ord('a')) * k + b) % 26 + ord('a')
        ans = ans + chr(a)
    print(ans)
    return ans 

def decode(k:int, b:int, msg:str):
    ans = ''
    ans = ''
    for i in msg:
        a = ((ord(i) - ord('a')) - b + 26) % 26
        k_, _, _ = exgcd(k, 26)
        a = (a * k_) % 26 + ord('a')
        ans = ans + chr(a)
    print(ans)
    return ans

k, b, msg, op = inputValue()
if checkKey(k):
    print('invalid key')
    exit()
if op == 1:
    encode(k, b, msg)
elif op == 0:
    decode(k, b, msg)
else:
    print('error operation!')
