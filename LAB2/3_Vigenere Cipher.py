def dirtCreate(n=26):
    d = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            d [i][j] = chr(ord('a') + (i + j) % 26 )
    # for m in d:
    #     print(m)
    return d 

def encode(d, key, msg):
    ans = ''
    for i in range(len(msg)):
        ans += d[ord(key[i])-ord('a')][ord(msg[i])-ord('a')]
    print(ans)
    return ans

def decode(d, key, msg):
    ans = ''
    for i in range(len(msg)):
        l = d[ord(key[i])-ord('a')]
        ans += chr(l.index(msg[i]) + ord('a'))
    print(ans)
    return ans

d = dirtCreate()
key = input().strip()
msg = input().strip()
op = int(input())
while len(key) <= len(msg):
    key += key
key = key[:len(msg)]

if op == 1:
    encode(d, key, msg)
elif op == 0:
    decode(d, key, msg)