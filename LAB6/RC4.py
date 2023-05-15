"""
 @description: RC4加密算法
 @author: Harrison-1eo
 @date: 2023-04-12
 @version: 1.0
"""


class RC4:
    def __init__(self, key: str):
        self.key = key
        key_list = self.str_to_list(key)
        self.s   = self.KSA(key_list)
        self.PRGA_i = 0
        self.PRGA_j = 0

    def str_to_list(self, msg: str):
        """
        convert a string to a list of int (0-255)
        :param msg: string, hex string
        :return: list of int (0-255)
        """
        msg = msg[2:] if msg.startswith('0x') else msg
        return [int(msg[i:i+2], 16) for i in range(0, len(msg), 2)]

    def init_key(self):
        """
        重新初始化密钥
        """
        key_list = self.str_to_list(self.key)
        self.s = self.KSA(key_list)
        self.PRGA_i = 0
        self.PRGA_j = 0

    def KSA(self, key: list):
        """
        Key Scheduling Algorithm
        :param key: list of int (0-255), length of key is 1-256
        :return: list of int (0-255), length of list is 256
        """
        j = 0
        s = [i for i in range(256)]
        t = [key[i % len(key)] for i in range(256)]
        for i in range(256):
            j = (j + s[i] + t[i]) % 256
            s[i], s[j] = s[j], s[i]
        return s       

    def PRGA_stepGenerator(self):
        """
        Pseudo Random Generation Algorithm, step generator
        PRGA每次调用的时候只生成一个字节，下次调用时会继续生成下一个字节
        :return: int (0-255)
        """
        while True:
            self.PRGA_i = (self.PRGA_i + 1) % 256
            self.PRGA_j = (self.PRGA_j + self.s[self.PRGA_i]) % 256
            self.s[self.PRGA_i], self.s[self.PRGA_j] = self.s[self.PRGA_j], self.s[self.PRGA_i]
            t = (self.s[self.PRGA_i] + self.s[self.PRGA_j]) % 256
            yield self.s[t]
    
    def encrypt_byte(self, byte: int):
        """
        encrypt a byte
        :param byte: int (0-255)
        :return: int (0-255)
        """
        return byte ^ next(self.PRGA_stepGenerator())
                  
    def encrypt_str(self, plaintext: str):
        """
        加密一个'0x'开头的16进制字符串，返回加密后的'0x'开头的16进制字符串
        :param plaintext: string, hex string
        :return: string, hex string
        """
        plaintext = self.str_to_list(plaintext)
        ciphertext = [self.encrypt_byte(byte) for byte in plaintext]
        return '0x' + ''.join([hex(i)[2:].zfill(2) for i in ciphertext])
    
    def encrypt_steam(self):
        """
        从键盘中读取'0x'开头的16进制字符串，加密后输出
        每次读取一个字节（2个16进制字符）
        """
        import sys
        # 先读取'0x'
        sys.stdin.read(2)
        sys.stdout.write('0x')

        # 每次读取一个字节
        while True:
            c = sys.stdin.read(1)
            if not c or c == '\n' or c == '\r':
                break
            else:
                d = sys.stdin.read(1)
            byte = int(c + d, 16)
            
            sys.stdout.write(hex(self.encrypt_byte(byte))[2:].zfill(2))

    def decrypt_byte(self, byte: int):
        """
        decrypt a byte
        :param byte: int (0-255)
        :return: int (0-255)
        """
        return self.encrypt_byte(byte)
    
    def decrypt_str(self, ciphertext: str):
        """
        decrypt a string
        :param ciphertext: string, hex string
        :return: string, hex string
        """
        return self.encrypt_str(ciphertext)
    
def main():
    key = input().strip() 
    rc4 = RC4(key)
    rc4.encrypt_steam()

if __name__ == '__main__':
    # key = '0x86c005ae8d42a1e8b012ce710e38d35672d6b4b41249975f69'
    # msg = '0x646d0ac40f7d0594'
    # rc4 = RC4(key)
    # ciphertext = rc4.encrypt_str(msg)
    # print(ciphertext)
    main()