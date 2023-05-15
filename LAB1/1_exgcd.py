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
    if gcd < 0:
        ppx, ppy, gcd = -ppx, -ppy, -gcd
    assert ppx * a + ppy * b == gcd
    # print(ppx ,a, ppy, b, gcd)
    return ppx, ppy, gcd

if __name__ == "__main__":
    i = input()
    list = i.split(" ")
    a = int(list[0])
    b = int(list[1])
    x, y, gcd = exgcd(a, b)
    while x <= 0:
        if b < 0:
            x -= b // gcd
            y += a // gcd
        else:
            x += b // gcd
            y -= a // gcd
    print(x, y, gcd, sep=' ')