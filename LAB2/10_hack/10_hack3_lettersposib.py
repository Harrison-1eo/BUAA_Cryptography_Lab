import random
import time
from math import log10
with open("msg.txt","r") as file:
    msg = file.read()
LENGTH = 10000

# 一个字典，字典内容为连续字符及其出现概率，并计算在当前字典下给定字符串的得分情况
class Dictionary(object):
    def __init__(self, txt: str):
        self.d = {}

        file = open(txt, "r")
        for line in file:
            key, count = line.split(' ')
            self.d[key] = int(count)

        self.length = len(key)
        self.total  = sum(iter(self.d.values()))
        
        # 计算每种连续字符出现概率的对数
        for key in self.d.keys():
            self.d[key] = log10(float(self.d[key])/self.total)

    # 计算在当前字典下给定字符串的得分情况
    def cal(self, msg: str):
        score = 0
        # 取出字符串中每个相邻的self.length长度的串，将其概率相加，返回结果
        ptr = 0

        while ptr + self.length < len(msg):
            if msg[ptr: ptr + self.length] in self.d:
                score += self.d[msg[ptr: ptr + self.length]]
            ptr += self.length
        return score

def takeSecond(elem):
    return elem[1]

# 首先统计文章的的字母频率，作为修改的基础，返回值为由元组构成的列表
def one_letter_frequency():
    alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num = [0] * 26
    result = []
    total = 0
    
    for i in msg:
        num[alp.index(i)] += 1
        total += 1

    for i in range(0,26):
        result.append((alp[i], num[i] / total))

    result.sort(key=takeSecond, reverse=True)
    for i in range(0,26):
        print(result[i][0],":",result[i][1] * 100)
    
    return [i[0] for i in result]

def decrypt(msg: str, one: list, mode: int):
    
    dictionary = Dictionary(str(mode) + '_letters_freq.txt')

    # maxkey = list('abcdefghijklmnopqrstuvwxyz')
    freq = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']

    # 计算直接以当前频率对应密钥的得分，以此为基准找得分比它高的
    maxscore = 0
    maxkey = [one[freq.index(chr(ord('a') + i))] for i in range(26)]
    trans = substitute(msg, maxkey)
    maxscore = dictionary.cal(trans)
    
    # 存储所有可能的结果，存储内容为由密钥和得分组成的元组
    posb_key_list = [] 
    posb_key_list.append((maxkey, maxscore))

    # random.shuffle(maxkey)

    count = 0
    # 进化过程中如果循环1000次没有进步，则认为已经得到最佳答案
    while count < 1000:
        
        # 在密钥中随机选取两个数进行交换
        a = random.randint(0, 25)
        b = random.randint(0, 25)
        child = list(maxkey[:])
        child[a], child[b] = child[b], child[a]

        # 计算新密钥下的得分
        trans = substitute(msg, child)
        score = dictionary.cal(trans)

        # 如果得分更高，则更新最佳得分，保存当前密钥，count置0开始新一轮的进化
        if score > maxscore:
            maxscore = score
            maxkey = list(child[:])
            posb_key_list.append((maxkey, maxscore))
            # print(count, a, b, score)
            count = 0

        count = count + 1

    # 将所有可能结果按得分排序，返回列表
    posb_key_list.sort(key=takeSecond, reverse=True)
    return posb_key_list    

# 替换，使用key单表替换text的内容
def substitute(inptext, key):
    output = ""
    for letter in inptext:
        output += chr(ord('a') + key.index(letter))
    return output

if __name__ == '__main__':
    start = time.time()

    one = one_letter_frequency()
	
	# 可以更改mode的值改变分段字母的长度，可以为2/3/4
    ans = decrypt(msg[:LENGTH], one, mode = 4)

    for a in ans[:10]:
        print("".join(a[0]), a[1])

    end = time.time()
    print('Running time: %s Seconds'%(end-start))