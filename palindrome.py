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
# print(sol.generatePalindromes('aabbcc'))

################ Valid Palindrome II ################
class Solution:
    """
    @param s: a string
    @return: nothing
    """
    def validPalindrome(self, s):
        left, right = self.twoPointer(s, 0, len(s) - 1)
        if left >= right:
            return True

        return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)

    def isPalindrome(self, s, left, right):
        left, right = self.twoPointer(s, left, right)
        return left >= right

    def twoPointer(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right

################ Palindrome Partitioning II ################
# 可以看作序列型动态规划问题, 设定 dp[i] 表示原串的前 i 个字符最少分割多少次可以使得到的都是回文子串.
# 如果 s 前 i 个字符组成的子串本身就是回文串, 则 dp[i] = 0, 否则:
# dp[i] = min{dp[j] + 1} (j < i 并且 s[j + 1], s[j + 2], ... , s[i] 是回文串)
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        n = len(s)
        f = []
        p = [[False for x in range(n)] for x in range(n)]
        #the worst case is cutting by each char
        for i in range(n+1):
            f.append(n - 1 - i) # the last one, f[n]=-1
        for i in reversed(range(n)):
            for j in range(i, n):
                if (s[i] == s[j] and (j - i < 2 or p[i + 1][j - 1])):
                    p[i][j] = True
                    f[i] = min(f[i], f[j + 1] + 1)
        return f[0]

################ Palindrome Partitioning ################
# Return all possible palindrome partitioning of s
class Solution:
    # 1. 使用 append + pop 的方式
    def partition(self, s):
        results = []
        self.dfs(s, [], results)
        return results

    def dfs(self, s, stringlist, results):
        if len(s) == 0:
            results.append(list(stringlist))
            return

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.is_palindrome(prefix):
                stringlist.append(prefix)
                self.dfs(s[i:], stringlist, results)
                stringlist.pop()

    def is_palindrome(self, s):
        return s == s[::-1]

    # 2. 使用记忆化搜索来做的办法，和 word break ii 类似
    def partition(self, s):
        return self.dfs(s, {})

    def dfs(self, s, memo):
        if s == "":
            return []
        if s in memo:
            return memo[s]

        partitions = []
        for i in range(len(s) - 1):
            prefix = s[:i + 1]
            if prefix != prefix[::-1]:
                continue

            sub_partitions = self.dfs(s[i + 1:], memo)
            for p in sub_partitions:
                partitions.append([prefix] + p)

        if s == s[::-1]:
            partitions.append([s])

        memo[s] = partitions
        return partitions

    # 3. 记忆化搜索来实现 get_is_palindrome
    def partition(self, s):
        results = []
        self.dfs(s, 0, [], {}, results)
        return results

    def generate_solution(self, s, partition):
        strings = []
        last_index = -1
        for i in partition:
            strings.append(s[last_index + 1: i + 1])
            last_index = i
        return strings

    def get_is_palindrome(self, memo, s, i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == j:
            return True
        if i + 1 == j:
            return s[i] == s[j]

        memo[(i, j)] = s[i] == s[j] and self.get_is_palindrome(memo, s, i + 1, j - 1)
        return memo[(i, j)]

    def dfs(self, s, index, partition, memo, results):
        if index == len(s):
            results.append(self.generate_solution(s, partition))
            return

        for i in range(index, len(s)):
            if not self.get_is_palindrome(memo, s, index, i):
                continue
            partition.append(i)
            self.dfs(s, i + 1, partition, memo, results)
            partition.pop()

    # dp
    def partition(self, s):
        results = []
        is_palindrome = self.get_is_palindrome(s)
        self.dfs(s, 0, [], is_palindrome, results)
        return results

    def generate_solution(self, s, partition):
        strings = []
        last_index = -1
        for i in partition:
            strings.append(s[last_index + 1: i + 1])
            last_index = i
        return strings

    def dfs(self, s, index, partition, is_palindrome, results):
        if index == len(s):
            results.append(self.generate_solution(s, partition))
            return

        for i in range(index, len(s)):
            if not is_palindrome[index][i]:
                continue
            partition.append(i)
            self.dfs(s, i + 1, partition, is_palindrome, results)
            partition.pop()

    def get_is_palindrome(self, s):
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(n - 1):
            is_palindrome[i][i + 1] = (s[i] == s[i + 1])

        for delta in range(2, n):
            for i in range(n - delta):
                j = i + delta
                is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]

        return is_palindrome
