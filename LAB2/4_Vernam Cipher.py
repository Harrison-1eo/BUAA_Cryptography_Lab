
def encode(key, msg):
    ans = ''
    for i in range(len(msg)):
        ans += chr(ord(key[i]) ^ ord(msg[i]))
    print(ans)
    return ans

key = input().strip()
msg = input().strip()
op = int(input())
while len(key) <= len(msg):
    key += key
key = key[:len(msg)]

if op == 1:
    encode(key, msg)
elif op == 0:
    encode(key, msg)