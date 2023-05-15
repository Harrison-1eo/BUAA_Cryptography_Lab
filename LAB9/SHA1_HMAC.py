"""
 @description: HMAC-SHA1算法实现
 @author: Harrison-1eo
 @date: 2023-05-04
 @version: 1.0
"""

from SHA1 import sha1


# 循环左移函数
def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff


# HMAC-SHA1算法主要函数
def sha1_hmac(key, message: bytes):
    # 将密钥和消息分别进行填充
    if len(key) > 64:
        key = sha1(key)
    key += b'\x00' * (64 - len(key))
    ipad = b'\x36' * 64
    opad = b'\x5c' * 64
    k_ipad = bytes([x ^ y for x, y in zip(key, ipad)])
    k_opad = bytes([x ^ y for x, y in zip(key, opad)])

    # 计算HMAC-SHA1值
    inner_hash = sha1(k_ipad + message)
    tmp = bytes.fromhex(inner_hash)
    outer_hash = sha1(k_opad + tmp)

    # 返回HMAC-SHA1值的十六进制表示
    return outer_hash


if __name__ == '__main__':
    # 用于测试的示例代码
    key = input().strip()
    key = bytes.fromhex(key)
    message = input().strip().encode('utf-8')
    mac = sha1_hmac(key, message)
    print(mac)
