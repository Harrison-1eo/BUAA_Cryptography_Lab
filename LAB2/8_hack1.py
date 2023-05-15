def listMax(l: list):
    max = l[0]
    ptr = 0
    for index, value in enumerate(l):
        if value > max:
            max = value
            ptr = index
    return ptr, max


d = [0 for _ in range(26)]
msg = input().strip()
for i in msg:
    d[ord(i) - ord('a')] += 1
ans = listMax(d)[0] - (ord('e') - ord('a'))

print (ans)
    
