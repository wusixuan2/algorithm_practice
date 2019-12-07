########################## Regular Expression Matching ##########################
# '.' Matches any single character
# '*' Matches zero or more of the preceding element
class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, source, pattern):
        return self.is_match_helper(source, 0, pattern, 0, {})

    # source 从 i 开始的后缀能否匹配上 pattern 从 j 开始的后缀
    # 能 return True
    def is_match_helper(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # source is empty
        if len(source) == i:
            return self.is_empty(pattern[j:])

        if len(pattern) == j:
            return False

        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            matched = self.is_match_char(source[i], pattern[j]) and self.is_match_helper(source, i + 1, pattern, j, memo) or \
                self.is_match_helper(source, i, pattern, j + 2, memo)
        else:
            matched = self.is_match_char(source[i], pattern[j]) and self.is_match_helper(source, i + 1, pattern, j + 1, memo)

        memo[(i, j)] = matched
        return matched


    def is_match_char(self, s, p):
        return s == p or p == '.'

    def is_empty(self, pattern):
        if len(pattern) % 2 == 1:
            return False

        for i in range(len(pattern) // 2):
            if pattern[i * 2 + 1] != '*':
                return False
        return True


##########################
class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    hash = None
    def isMatch(self, s, p):
        if self.hash is None:
            self.hash = {}
        key = s + p
        if key in self.hash:
            return self.hash[key]

        if p == '':              #如果p串为空
            return s == ''       #判断s串是否为空
        if s == '':              #如果s串为空
            if len(p) % 2 == 1:
                return False
            i = 1
            while i < len(p):    #需要满足"x*x*"的形式
                if p[i] != '*':
                    return False
                i += 2
            return True

        if len(p) > 1 and p[1] == '*':   #如果p串中的当前字符为'*'
            if p[0] == '.':              #如果p中为.
                self.hash[key] = self.isMatch(s[1:], p) or self.isMatch(s, p[2:]) #.去匹配s[0]并且''||.和*不去匹配，用p[2]匹配
            elif p[0] == s[0]:
                self.hash[key] = self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                self.hash[key] = self.isMatch(s, p[2:])
        elif p[0] == '.':
            self.hash[key] = self.isMatch(s[1:], p[1:])  #继续向下匹配
        else:
            self.hash[key] = s[0] == p[0] and self.isMatch(s[1:], p[1:])  #继续向下匹配

        return self.hash[key]

class Solution(object):
    # DP
    def isMatch(self, s, p):
        dp = [[False for i in range(0,len(p) + 1)] for j in range(0, len(s) + 1)]
        dp[0][0] = True   #dp[0][0]初始化为true，由此开始转移
        for i in range(1, len(p) + 1):
            if (p[i - 1] == '*'):
                dp[0][i] = dp[0][i - 2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':  #'*'不去匹配
                        dp[i][j] |= dp[i-1][j]
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':  #如果两字符相同或者为.
                        dp[i][j] = dp[i - 1][j - 1]    #当前状态由前一个转移而来

        return dp[len(s)][len(p)]

    # 懒癌版
    def isMatch(self, s, p):
        return re.match(p + '$', s) != None



########################## 通配符匹配 ##########################
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    #### solution 1
    def isMatch(self, source, pattern):
        return self.is_match_helper(source, 0, pattern, 0, {})

    # source 从 i 开始的后缀能否匹配上 pattern 从 j 开始的后缀
    # 能 return True
    def is_match_helper(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # source is empty
        if len(source) == i:
            # every character should be "*"
            for index in range(j, len(pattern)):
                if pattern[index] != '*':
                    return False
            return True

        if len(pattern) == j:
            return False

        if pattern[j] != '*':
            matched = self.is_match_char(source[i], pattern[j]) and \
                self.is_match_helper(source, i + 1, pattern, j + 1, memo)
        else:
            matched = self.is_match_helper(source, i + 1, pattern, j, memo) or \
                self.is_match_helper(source, i, pattern, j + 1, memo)

        memo[(i, j)] = matched
        return matched


    def is_match_char(self, s, p):
        return s == p or p == '?'


    #### solution 2
    def isMatch(self, s, p):
        n = len(s)
        m = len(p)
        f = [[False] * (m + 1) for i in range(n + 1)]
        f[0][0] = True

        if n == 0 and p.count('*') == m:
            return True

        for i in range(0, n + 1):
            for j in range(0, m + 1):
                if i > 0 and j > 0:
                    f[i][j] |= f[i-1][j-1] and (s[i-1] == p[j-1] or p[j - 1] in ['?', '*'])

                if i > 0 and j > 0:
                    f[i][j] |= f[i - 1][j] and p[j - 1] == '*'

                if j > 0:
                    f[i][j] |= f[i][j - 1] and p[j - 1] == '*'


        return f[n][m]

# Function to get minimum number of trials
# needed in worst case with n eggs and k floors
# K: number of egg, N: number of floor
def superEggDrop(K: int, N: int):

    memo = dict()
    def dp(K, N) -> int:
        # base case
        if K == 1: return N
        if N == 0: return 0
        # 避免重复计算
        if (K, N) in memo:
            return memo[(K, N)]

        res = float('INF')
        # 穷举所有可能的选择
        for i in range(1, N + 1):
            res = min(res,
                      max(
                            dp(K, N - i), # 碎
                            dp(K - 1, i - 1) # 没碎
                         ) + 1 # 在第 i 楼扔了一次
                  )
        # 记入备忘录
        memo[(K, N)] = res
        return res
    return dp(K, N)

# Input: [4, 1, 1, 4]
# Output: 18
# Explanation:
#   1. Merge second and third piles => [4, 2, 4], score = 2
#   2. Merge the first two piles => [6, 4]，score = 8
#   3. Merge the last two piles => [10], score = 18
# 使用四边形不等式优化之后的算法，时间复杂度 O(n^2)
# 记录 cut[i][j] 代表使得 dp[i][j] 获得最优值的那个划分方案（切割位置）
# 可以证明cut[i][j - 1] <= cut[i][j] <= cut[i + 1][j]
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        n = len(A)
        if n < 2:
            return 0

        # dp[i][j] => minimum cost merge from i to j
        dp = [[0] * n for _ in range(n)]
        # cut[i][j] => the best middle point that make dp[i][j] has the minimum cost
        cut = [[0] * n for _ in range(n)]
        # range_sum[i][j] => A[i] + A[i + 1] ... + A[j]
        range_sum = self.get_range_sum(A)

        for i in range(n - 1):
            dp[i][i + 1] = A[i] + A[i + 1]
            cut[i][i + 1] = i

        # enumerate the range size first, start point second
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = sys.maxsize
                for mid in range(cut[i][j - 1], cut[i + 1][j] + 1):
                    if dp[i][j] > dp[i][mid] + dp[mid + 1][j] + range_sum[i][j]:
                        dp[i][j] = dp[i][mid] + dp[mid + 1][j] + range_sum[i][j]
                        cut[i][j] = mid

        return dp[0][n - 1]

    def get_range_sum(self, A):
        n = len(A)
        range_sum = [[0] * n for _ in range(len(A))]
        for i in range(n):
            range_sum[i][i] = A[i]
            for j in range(i + 1, n):
                range_sum[i][j] = range_sum[i][j - 1] + A[j]
        return range_sum
