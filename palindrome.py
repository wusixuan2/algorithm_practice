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

# longestPalindromeSubseq('bbbab')

################ 回文排列II  · Palindrome Permutation II ################
import collections
import itertools
class Solution:
    """
    @param s: the given string
    @return: all the palindromic permutations (without duplicates) of it
    """
    # check if palindrome exists.
    # find the permutation of one of the haves of char
    # for each permutation, reversed the string, and concatenate with the original one.
    def generatePalindromes1(self, s):
        counter = collections.Counter(s)
        odds = list(filter(lambda x: x % 2, counter.values()))
        if len(odds) > 1:
            return []
        baseStr, mid = self.preProcess(counter)
        return self.backTracking(baseStr, 0, mid, [baseStr + mid + baseStr[::-1]])

    def preProcess(self, counter):
        baseStr = mid = ""
        for char in counter:
            if counter[char] % 2:
                mid = char
            baseStr += char*(counter[char]//2)
        return baseStr, mid

    # O(2^n) DFS backtracking.
    def backTracking(self, s, idx, mid, ans):
        if idx == len(s) - 1:
            return ans

        for i in range(idx, len(s)):
            if i >= 1 and s[i] == s[i-1] == s[idx]:
                continue #no need to go deeper if swap would be the same
            #Swap s[idx] with s[i]
            if i != idx:
                permu = s[:idx] + s[i] + s[idx+1:i] + s[idx] + s[i+1:]
                ans.append(permu + mid + permu[::-1])
            else:
                permu = s
            self.backTracking(permu, idx+1, mid, ans)
        return ans
    ######
    def generatePalindromes(self, s):
        cnt = collections.Counter(s)
        mid = ''.join(k for k, v in cnt.items() if v % 2)
        chars = ''.join(k * (v // 2) for k, v in cnt.items())
        return self.permuteUnique(mid, chars) if len(mid) < 2 else []

    def permuteUnique(self, mid, nums):
        result = []
        used = [False] * len(nums)
        self.permuteUniqueRecu(mid, result, used, [], nums)
        return result

    def permuteUniqueRecu(self, mid, result, used, cur, nums):
        if len(cur) == len(nums):
            half_palindrome = ''.join(cur)
            result.append(half_palindrome + mid + half_palindrome[::-1])
            return
        for i in range(len(nums)):
            if not used[i] and not (i > 0 and nums[i-1] == nums[i] and used[i-1]):
                used[i] = True
                cur.append(nums[i])
                self.permuteUniqueRecu(mid, result, used, cur, nums)
                cur.pop()
                used[i] = False
    ######
    def generatePalindromes2(self, s):
      cnt = collections.Counter(s)
      mid = tuple(k for k, v in cnt.items() if v % 2)
      chars = ''.join(k * (v // 2) for k, v in cnt.items())
      return [''.join(half_palindrome + mid + half_palindrome[::-1]) \
        for half_palindrome in set(itertools.permutations(chars))] if len(mid) < 2 else []

sol = Solution()
print(sol.generatePalindromes('aabbcc'))
