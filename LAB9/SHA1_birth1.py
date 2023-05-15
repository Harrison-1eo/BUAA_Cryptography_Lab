"""
 @description: SHA1的第一类生日攻击
 @author: Harrison-1eo
 @date: 2023/5/09
 @version: 1.0
"""

import hashlib
import random


n = int(input()) // 4
target = input().strip()
target_hash = bytes.fromhex(target)[:n]


massage = b'I am carrying out a first order birthday attack on SHA1 and have already succeeded in the attack'


ori = massage
orilen = len(massage)

while True:
    mlen = len(massage)

    insert = random.randint(0, mlen)
    insert_letter = random.randint(65, 90).to_bytes(1, 'big')
    insert_number = random.randint(0, 2)

    massage = massage[:insert] + insert_letter * insert_number + massage[insert:]

    hash = hashlib.sha1(massage).digest()

    if hash[:n] == target_hash:
        print(massage.decode())
        # print(hash)
        break


