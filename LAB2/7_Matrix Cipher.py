def encrypt(key_len:int, key:list, msg:str):
    ans = ''
    d = []
    num = len(msg) // key_len
    left = len(msg) - key_len * num
    ptr = 0
    for _ in range(num):
        d.append(msg[ptr: ptr + key_len])
        ptr += key_len
    if left != 0:
        d.append(msg[ptr: ])
    for k in range(key_len):
        i = key.index(str(k + 1))
        for j in range(num if left == 0 else num + 1):
            if i < len(d[j]):
                ans += d[j][i]
    return ans

def decrypt(key_len:int, key:list, msg:str):
    ans = ''
    num = len(msg) // key_len
    d = [[0] * key_len for _ in range(num)]
    ptr = 0
    for k in range(key_len):
        i = key.index(str(k + 1))
        for j in range(num):
            d[j][i] = msg[ptr]
            ptr += 1
    for i in d:
        for j in i:
            ans += j
    return ans



key_len = int(input())
key = input()
msg = input().strip()
op = int(input())
if op == 1:
    ans = encrypt(key_len, list(key[::1]), msg)
elif op == 0:
    ans = decrypt(key_len, list(key[::1]), msg)
print(ans)
