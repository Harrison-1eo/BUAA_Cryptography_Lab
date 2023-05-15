"""
 @description: SHA1的第二类碰撞攻击，不同的更改方式，使得hash值相同
 @author: Harrison-1eo
 @date: 2023/5/11
 @version: 1.0
"""

import hashlib
import random
import time


def sha1(msg: bytes) -> bytes:
    return hashlib.sha1(msg).digest()


def sha1_birth2_num(msg: bytes):
    hash_dict = {}

    while True:
        # 一个0.9-1的数
        random_number = (random.random() * 0.1 + 0.9) * 100

        number = str(random_number).encode('utf-8')
        message = msg + number

        h = hashlib.sha1(message).digest()[:4]
        if h in hash_dict:
            if hash_dict[h] == message:
                continue
            return hash_dict[h], message, h

        else:
            hash_dict[h] = message


def sha1_birth2_char(message: bytes):
    hash_dict = {}

    ori = message
    orilen = len(message)

    while True:
        mlen = len(message)
        if mlen > orilen * 1.3:
            message = ori

        insert = random.randint(0, mlen)
        insert_letter = random.randint(42, 47).to_bytes(1, 'big')
        insert_number = random.randint(0, 2)

        message = message[:insert] + insert_letter * insert_number + message[insert:]

        h = sha1(message)[:4]
        if h in hash_dict:
            if hash_dict[h] == message:
                continue
            return hash_dict[h], message, h

        else:
            hash_dict[h] = message


def sha1_birth2_space(message: bytes):
    hash_dict = {}

    ori = message
    orilen = len(message)
    while True:
        mlen = len(message)
        if mlen > orilen * 1.3:
            message = ori

        insert = random.randint(0, mlen)
        insert_letter = random.randint(32, 126).to_bytes(1, 'big')
        insert_letter = insert_letter + b'\x08'

        message = message[:insert] + insert_letter + message[insert:]

        h = sha1(message)[:4]
        if h in hash_dict:
            if hash_dict[h] == message:
                continue
            return hash_dict[h], message, h

        else:
            hash_dict[h] = message


if __name__ == '__main__':

    ori1 = b'I am attempting a second order birthday attack on SHA one'
    ori2 = b' I have now successfully found messages that implement the birthday attack on SHA one'
    ori3 = b'My final grade for the cryptography laboratory course is '

    start = time.time()

    res1, res2, hash4 = sha1_birth2_space(ori1)
    print('message1 =', res1)
    print('message2 =', res2)
    print('message1(ascii)= ', res1.decode('ascii'))
    print('message2(ascii)= ', res2.decode('ascii'))
    print('hash1 =', hash4)
    print('=======================================')
    res1, res2, hash4 = sha1_birth2_char(ori2)
    print('message3 =', res1)
    print('message4 =', res2)
    print('hash2 =', hash4)
    print('=======================================')
    res1, res2, hash4 = sha1_birth2_num(ori3)
    print('message5 =', res1)
    print('message6 =', res2)
    print('hash3 =', hash4)
    print('=======================================')
    print('time= ', time.time() - start)
