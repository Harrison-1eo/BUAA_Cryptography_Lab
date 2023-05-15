def encrypt(key:int, length:int, msg:str): 
    ans = ''
    d = ['' for _ in range(key)]
    for i in range(len(msg)):
        d[i % key] += msg[i]
    for j in d:
        ans += j
    return ans

def decrypt(key:int, length:int, msg:str): 
    ans = ''
    d = []
    left = len(msg) - key * length
    ptr = 0
    for _ in range(left):
        d.append(msg[ptr: ptr + length + 1])
        ptr += length + 1
    for _ in range(key - left):
        d.append(msg[ptr: ptr + length])
        ptr += length
    for i in range(length+1):
        for j in range(key):
            if i < len(d[j]):
                ans += d[j][i]

    return ans


key = int(input())
msg = input().strip()
op = int(input())
if op == 1:
    ans = encrypt(key, len(msg)//key, msg)
elif op == 0:
    ans = decrypt(key, len(msg)//key, msg)

print(ans)