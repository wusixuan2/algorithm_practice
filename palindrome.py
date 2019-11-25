################# Longest Palindromic Subsequence #################
# 1. 如果头尾字符相同，那么字符串的最长子序列等于去掉首尾的字符串的最长子序列加上首尾
# dp[i][j]=dp[i+1][j−1]+2 if(str[i]==str[j])
# 2. 如果首尾字符不同，则最长子序列等于去掉头的字符串的最长子序列和去掉尾的字符串的最长子序列的较大者。
# dp[i][j]=max(dp[i+1][j],dp[i][j−1])if(str[i]!=str[j])
def longestPalindromeSubseq(s):
  if not s: return 0

  dp = len(s) * [0]
  last, current = 0, 0
  for i in range(len(s) - 1, -1, -1):
    for j in range(i, len(s)):
      if i == j: current = 1
      else:
        current = last + 2 if s[i] == s[j] else max(dp[j], dp[j-1])
      last = dp[j]
      dp[j] = current
  return dp[len(s)-1]

longestPalindromeSubseq('bbbab')
