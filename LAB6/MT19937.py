"""
 @description: MT19937加密算法
 @author: Harrison-1eo
 @date: 2023-04-12
 @version: 1.0
"""


class MT19937:
    def __init__(self, seed):
        self.seed = seed
        self.mt = self.initialize(seed)
        self.twist()
        self.mti = 0

    def initialize(self, seed):
        mt = [0] * 624
        mt[0] = seed
        for i in range(1, 624):
            mt[i] = (1812433253 * (mt[i - 1] ^ mt[i - 1] >> 30) + i) & 0xFFFFFFFF
        return mt
    
    def twist(self):
        for i in range(0, 624):
            y = ((self.mt[i] & 0x80000000) + (self.mt[(i + 1) % 624] & 0x7fffffff)) & 0xFFFFFFFF
            self.mt[i] = (y >> 1) ^ self.mt[(i + 397) % 624]

            if y % 2 != 0:
                self.mt[i] = self.mt[i] ^ 0x9908b0df

    def extract_number(self):
        y = self.mt[self.mti]
        y = y ^ y >> 11
        y = y ^ y << 7 & 2636928640
        y = y ^ y << 15 & 4022730752
        y = y ^ y >> 18
        self.mti = (self.mti + 1) % 624
        return y & 0xFFFFFFFF

if __name__ == '__main__':
    seed = int(input())
    mt   = MT19937(seed)
    for _ in range(20):
        print( mt.extract_number() )

    