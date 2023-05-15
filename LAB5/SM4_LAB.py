import SM4_MODE as sm4

# 随机生成一个128位的密钥
def generate_key():
    import random
    key = []
    for i in range(16):
        key.append(hex(random.randint(0, 255))[2:].zfill(2))
    return int(''.join(key), 16)

filename = 'pic_original.bmp'
with open(filename, 'rb') as f:
    bytes_data = f.read()

header = bytes_data[:54]
msg = bytes_data[54:]

plaintext = []
for i in range(len(msg)):
    plaintext.append(hex(msg[i])[2:].zfill(2))

key = generate_key()
iv  = generate_key()
print('key: ', hex(key))
print('iv: ', hex(iv))

run = sm4.SM4_MODE(key)

# ==================== ECB ====================
ciphertext = run.encrypt(plaintext, 'ECB')

ans = ''.join(ciphertext)
with open('pic_ECB_encrypted.bmp', 'wb') as f:
    f.write(header)
    f.write(bytes.fromhex(ans))
print('ECB encryption done.')

# ==================== CBC ====================
ciphertext = run.encrypt(ciphertext, 'CBC', iv)

ans = ''.join(ciphertext)
with open('pic_CBC_decrypted.bmp', 'wb') as f:
    f.write(header)
    f.write(bytes.fromhex(ans))
print('CBC decryption done.')