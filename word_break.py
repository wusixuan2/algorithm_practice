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

sol = Solution()
print(sol.wordBreak("lintcode",["lint", "code"]))
print(sol.wordBreak("a",["b"]))
print(sol.wordBreak("aaaaaaa", ["aaaa","aaa"]))
