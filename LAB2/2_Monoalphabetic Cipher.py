def dircCreate():
    d = dict()
    a = input().strip()
    b = input().strip()
    for i in range(len(a)):
        d[a[i]] = b[i]
    return d

def encode(d: dict, msg: str):
    ans = ''
    for i in msg:
        ans += d[i]
    print(ans)
    return ans

def decode(d: dict, msg: str):
    ans = ''
    for i in msg:
        ans += list(d.keys())[list(d.values()).index(i)]
    print(ans)
    return ans

d = dircCreate()
msg = input().strip()
op = int(input())
if op == 1:
    encode(d, msg)
elif op == 0:
    decode(d, msg)