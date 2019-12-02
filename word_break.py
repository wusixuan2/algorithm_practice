class Solution:
    # Example:
    # Input:  "lintcode", ["lint", "code"]
    # Output:  true
    # 透過建立長度為n + 1的dp list
    # dp[j]若為True 表示該數列可以透過dictionary組出0~j的字串
    # dp = [False for _ in xrange(n + 1)]
    # dp的狀態為：
    # 從字的起點j 到字的終點i
    # 如果可以透過dictionary組出0~j的字串(dp[j] == True)且s[j:i]在dictionary裡面
    # 則可推出dp[i]是True
    # 最後回傳dp[n]
    # 這題的優化在兩個地方

    # 若dp[i]已經為真 就break掉不需要剩下的計算 -> 原因是我們只需要知道有一種方法可以走到i即可
    # 從i往回走j的長度最多也只可能是i-maxLen -> 不可能有比maxLen更長的dictionary key
    # 沒有這兩個優化都會TLE

    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        if len(dict) == 0:
            return len(s) == 0

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        maxLength = max([len(w) for w in dict])
        for i in range(1, n + 1):
            for j in range(1, min(i, maxLength) + 1):
                if not dp[i - j]:
                    continue
                if s[i - j:i] in dict:
                    dp[i] = True
                    break
        return dp[n]

    # BFS
    def wordBreakBFS(self, s, dict):
        if len(dict) == 0:
            return len(s) == 0

        n = len(s)
        maxLength = max([len(w) for w in dict])

        # BFS
        from collections import deque
        q = deque()
        hash = set()

        q.append(0)
        hash.add(0)

        while q:
            start = q.pop()
            for end in range(start + 1, min(start + maxLength, n) + 1):
                if end in hash:
                    continue

                if s[start:end] in dict:
                    if end == n:
                        return True
                    q.append(end)
                    hash.add(end)

        return False

    # return the number of sentences you can form
    # f[i] 代表子串 s[:i-1] 能被分割成多少个句子
    def wordBreak3(self, s, dict):
        if len(s) == 0 or len(dict) == 0:
            return 0

        dict_lower = set()
        for word in dict:
            dict_lower.add(word.lower())

        n = len(s)
        max_len = max([len(word) for word in dict])

        # define f[i]: number of sentences that s[:i - 1] can be breaked into using words in dic
        f = [0 for _ in range(n + 1)]

        # init
        f[0] = 1

        for i in range(1, n + 1):
            for j in range(0, i):
                if s[j:i].lower() in dict_lower:
                    f[i] += f[j]
        return f[-1]

    # 记忆化搜索剪枝
    # 利用memo[s]记录字符串s的切分方案，每次不断递归，枚举i为s的切割点进行搜索，一旦memo[s]存在，返回即可
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreakII(self, s, word_dict):
        return self.dfs(s, word_dict, {})

    # 找到 s 的所有切割方案并 return
    def dfs(self, s, word_dict, memo):
        if s in memo: return memo[s]
        if not s: return []

        partitions = []

        # 取整个字符串s
        if s in word_dict:
            partitions.append(s)

        # 取字符串s的前缀子串作为word，word长度为1到len(s) - 1
        for i in range(1, len(s)):
            prefix = s[:i]

            if prefix not in word_dict:
                continue

            sub_partitions = self.dfs(s[i:], word_dict, memo)
            for sub_partition in sub_partitions:
                partitions.append(prefix + " " + sub_partition)

        memo[s] = partitions
        return partitions

sol = Solution()
print(sol.wordBreakII("lintcode",["lint", "code"]))
print(sol.wordBreakII("a",["b"]))
print(sol.wordBreakII("aaaaaaa", ["aaaa","aaa"]))
