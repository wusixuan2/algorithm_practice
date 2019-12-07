prime = 101
def pattern_matching(text, pattern):
    m = len(pattern)
    n = len(text)
    pattern_hash = create_hash(pattern, m - 1)
    text_hash = create_hash(text, m - 1)

    for i in range(1, n - m + 2):
        if pattern_hash == text_hash:
            if check_equal(text[i-1:i+m-1], pattern[0:]) is True:
                return i - 1;
        if i < n - m + 1:
            text_hash = recalculate_hash(text, i-1, i+m-1, text_hash, m)
    return -1;

def check_equal(str1, str2):
    if len(str1) != len(str2):
        return False;
    i = 0
    j = 0
    for i, j in zip(str1, str2):
        if i != j:
            return False;
    return True

def create_hash(input, end):
    hash = 0
    for i in range(end + 1):
        hash = hash + ord(input[i])*pow(prime, i)
    return hash

def recalculate_hash(input, old_index, new_index, old_hash, pattern_len):
    new_hash = old_hash - ord(input[old_index])
    new_hash = new_hash/prime
    new_hash += ord(input[new_index])*pow(prime, pattern_len - 1)
    return new_hash;


index = pattern_matching("TusharRoy", "sharRoy")
print("Index ", index)
index = pattern_matching("TusharRoy", "Roy")
print("Index ", index)
index = pattern_matching("TusharRoy", "shar")
print("Index ", index)
index = pattern_matching("TusharRoy", "usha")
print("Index ", index)
index = pattern_matching("TusharRoy", "Tus")
print("Index ", index)
index = pattern_matching("TusharRoy", "Roa")
print("Index ", index)

# 数据结构:
# hash_t, hash_s: 子串哈希值, 长度 len(t)

# 初始化:
# base = 31
# MOD = 10 ** 7
# power = base ** len(t) % MOD
# hash_t = hash_s = 0

# 缩写 t: target, s: source

# 采用字符串哈希,将字符串映射为数字，
# hash_t = (hash_t * 26 + ord(t[i]) % MOD; 哈希函数, 字符串转化成数字.
# 对于要匹配的子串算出一个哈希值，然后再遍历主串,
# 循环, i 从 len(t) 开始,
# 利用滑动窗口, 维护中间 len(t) 长度的子串的哈希值, 子串 s[i - len(t): i],

# 加进低位, 滚动累乘, hash_s = hash_s * base + ord(s[i])
# 减去高位, - power * ord(s[i - nt]
# 如果与 target 串相同, 哈希本身不安全, 取出来 lent(t) 长度的子串再进行比较, 完全相同即可.
# 注意, 减高位 取模, 可能得到负数, 需要加 MOD, 将负数变为正数。
class Solution:
    def strStr2(self, source, target):
        s, t = source, target
        if t is None or s is None:
            return -1
        ns, nt = len(s), len(t)
        if nt > ns:
            return -1
        base = 31
        MOD = 10 ** 7
        power = 31**nt % MOD
        ht = hs = 0
        for i in range(nt):
            ht = (ht * base + ord(t[i])) % MOD
            hs = (hs * base + ord(s[i])) % MOD
        for i in range(nt, ns + 1):
            if ht == hs and s[i - nt: i] == t:
                return i - nt
            if i == ns:
                return -1
            hs = (hs * base + ord(s[i])) % MOD
            hs = (hs - power * ord(s[i - nt])) % MOD
            if hs < 0:
                hs += MOD
