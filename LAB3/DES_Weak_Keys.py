class WEAK_KEYS:
    def __init__(self, key):
        self.key = key
        self.subkey = self.key_gen(key)
        if self.subkey[0] == self.subkey[1]:
            self.nature = 'weak'
        else:
            self.nature = 'anti-weak'

    def key_gen(self, key):
        SHIFT =    [ 1,  1,  2,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  2,  1]
        key_list = []
        key_c = key[ :28]
        key_d = key[28: ]
        for i in SHIFT:  
            key_c = self.key_rotate_left(key_c, i)
            key_d = self.key_rotate_left(key_d, i)
            key_ch2 = self.key_choose2(key_c + key_d)
            key_list.append(key_ch2)
        return key_list
    
    # both halves are rotated left by one or two bits
    def key_rotate_left(self, key: str, n: int):
        return key[n: ] + key[: n]

    # 48 subkey bits are selected by Permuted Choice 2
    def key_choose2(self, key: str):
        KEY_PC2 =  [14, 17, 11, 24,  1,  5,  3, 28, 15,  6, 21, 10,
            23, 19, 12,  4, 26,  8, 16,  7, 27, 20, 13,  2,
            41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
        res = ''
        for i in KEY_PC2:
            res += key[i - 1]
        return res


anti = []
weak = []
ans = []

def get_weak_keys():
    import itertools

    # pob = ['00'*14, '01'*14, '10'*14, '11'*14]
    pob = []
    for i in range(2):
        for j in range(2):
            pob.append((str(i) + str(j)) * 14)

    # 两两组合，返回列表
    pob_comb = list(itertools.product(pob, repeat=2))
    # 将两两组合拼接成56位的key
    pob_comb = [i[0]+i[1] for i in pob_comb]


    for i in pob_comb:
        # 每个key生成16个子key，并判断是否为弱密钥
        key = WEAK_KEYS(i)
        if key.nature == 'anti-weak':
            anti.append(key)
        else:
            weak.append(key)

    # 两两组合可能的anti-weak keys
    anti_comb = list(itertools.product(anti, repeat=2))

    # 如果两个anti-weak keys的第一个子key的最后一位和第二个子key的第一位相同，则为anti-weak keys
    # 但是有重复的，要注意去掉

    for i in anti_comb:
        if i[0].subkey[0] == i[1].subkey[15]:
            t = tuple(sorted([i[0], i[1]], key=lambda x: x.key))
            if t not in ans:
                ans.append(t)

KEY_PC1 =  [57, 49, 41, 33, 25, 17,  9,  1, 58, 50, 42, 34, 26, 18,
            10,  2, 59, 51, 43, 35, 27, 19, 11,  3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,  7, 62, 54, 46, 38, 30, 22,
            14,  6, 61, 53, 45, 37, 29, 21, 13,  5, 28, 20, 12,  4]

# PC1 的逆运算
def key_ch1_inv(key: str):
    ans = ['0'] * 64
    for i in range(56):
        ans[KEY_PC1[i] - 1] = key[i]
    return ''.join(ans)

# 奇偶校验
def even_odd_test(key: str, mode: str):
    ans = ''
    key_slice = [key[i:i+8] for i in range(0, 64, 8)]
    for i in key_slice:
        count = i.count('1')
        ans += i[:7]
        ans += '1' if count % 2 == (mode == 'even') else '0'  
    return '0x' + hex(int(ans, 2))[2:].rjust(16, '0')

def print_print_ans():

    # print('weak-keys:')
    for i in weak:
        print('print(\'' + even_odd_test(key_ch1_inv(i.key), 'even') + '\')')
        print('print(\'' + even_odd_test(key_ch1_inv(i.key), 'odd')  + '\')')

    # print('anti-weak-keys:')
    for i in ans:
        print('print(\'' + even_odd_test(key_ch1_inv(i[0].key), 'even'), even_odd_test(key_ch1_inv(i[1].key), 'even') + '\')')
        print('print(\'' + even_odd_test(key_ch1_inv(i[0].key), 'odd'),  even_odd_test(key_ch1_inv(i[1].key), 'odd') + '\')')


def print_ans():
    # print('weak-keys:')
    for i in weak:
        print(even_odd_test(key_ch1_inv(i.key), 'even'))
        print(even_odd_test(key_ch1_inv(i.key), 'odd'))

    # print('anti-weak-keys:')
    for i in ans:
        print(even_odd_test(key_ch1_inv(i[0].key), 'even'), even_odd_test(key_ch1_inv(i[1].key), 'even'))
        print(even_odd_test(key_ch1_inv(i[0].key), 'odd'),  even_odd_test(key_ch1_inv(i[1].key), 'odd'))

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph.config import Config
from pycallgraph import GlobbingFilter


if __name__ == '__main__':
    graphviz = GraphvizOutput()
    graphviz.output_file = '3-1.png'
    with PyCallGraph(output=graphviz):

        get_weak_keys()
        print_ans()
        # print_print_ans()
