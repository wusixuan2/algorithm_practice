import sys
import math
import bisect
class Node:
  def __init__(self, value, left=None, right=None):
    self.left =left
    self.val = value
    self.right = right

class Solution:
  # time: O(mn) space: O(mn)
  def minPathSumRecursion(self, grid):
    x_end = len(grid) - 1
    y_end = len(grid[0]) - 1
    return self.findMin(grid, x_end, y_end)

  def findMin(self, grid, x, y):
    if x < 0 or y < 0:
      return sys.maxsize
    if x == 0 and y == 0:
      return grid[0][0]
    return grid[x][y] + min(self.findMin(grid, x,y-1), self.findMin(grid, x - 1, y))

  # Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
  # Note: You can only move either down or right at any point in time.
  # Dp[i][j] 存储从（0， 0） 到（i, j）的最短路径。
  # Dp[i][j] = min(Dp[i-1][j]), Dp[i][j-1]) + grid[i][j];
  def minPathSum(self, grid):
    m, n = len(grid), len(grid[0])
    dp = [0] + [sys.maxsize] * (n - 1)
    for i in range(m):
      for j in range(n):
        if j == 0:
          dp[j] = dp[j] + grid[i][j]
        else:
          dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
    return dp[n - 1]

  """
  @param root: The root of binary tree.
  @return: An integer
  """
  def maxPathSum(self, root):
    self.maxPath = -sys.maxsize-1
    self.dfs(root, self.maxPath)
    return self.maxPath

  def dfs(self, root, maxPath):
    if root == None: return 0
    left = self.dfs(root.left, self.maxPath)
    right = self.dfs(root.right, self.maxPath)
    self.maxPath = max(self.maxPath, root.val + left +right)
    return max(left, right) + root.val

  ###################
  def backPackRecursionWrapper(self, m, A, V):
    return self.backPackRecursion(A, V, m, 0)

  def backPackRecursion(self, weight, value, capacity, i):
    if i == len(weight) or capacity == 0:
      return 0
    elif weight[i] > capacity:
      return self.backPackRecursion(weight, value, capacity, i+1)
    else:
      return max(self.backPackRecursion(weight, value, capacity, i+1),
        value[i] +
        self.backPackRecursion(weight, value, capacity - weight[i], i+1))

  def knapsack(self, capacity, weight, value):
    n = len(weight)
    dp = [[0]*(capacity+1) for i in range(n+1)]

    for i in range(n+1):
      for j in range(capacity+1):
        if i == 0 or j == 0:
          dp[i][j] = 0
        elif weight[i-1] > j:
          dp[i][j] = dp[i-1][j]
        else:
          dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]]+ value[i-1])
    return dp[len(weight)][capacity]

  # @param m: An integer m denotes the size of a backpack
  # @param A & V: Given n items with size A[i] and value V[i]
  def backPackII(self, m, A, V):
      f = [0] * (m + 1)
      n = len(A)
      for i in range(n):
          for j in range(m, A[i]-1, -1):
            f[j] = max(f[j], f[j-A[i]] + V[i])
          print(f)
      return f[m]

  def uniquePaths(self, m, n):
    dp = [0] * n
    for r in range(m):
      for c in range(n):
        if (r == 0) or (c == 0):
          dp[c] = 1
        else:
          dp[c]= dp[c-1]+dp[c]
    return dp[n-1]

  def uniquePathsWithObstacles(self, obstacleGrid):
      if not obstacleGrid or len(obstacleGrid) == 0 or not obstacleGrid[0] or len(obstacleGrid[0]) == 0:
          return 0
      m, n = len(obstacleGrid), len(obstacleGrid[0])
      dp = [0] * n
      dp[0] = 1

      for i in range(m):
          for j in range(n):
              if obstacleGrid[i][j] == 1:
                  dp[j] = 0
              elif i > 0 and j > 0:
                  dp[j] += dp[j - 1]
              elif j > 0:
                  dp[j] = dp[j - 1]

      return dp[n - 1]

  # 考虑最后一步走1阶还是走2阶。
  # 方案数Dp[n] = 最后一步走1阶的方案数 + 最后一步走2阶的方案数。
  # Dp[n] = Dp[n-1] + Dp[n-2].
  def climbStairs(self, n):
    if n == 0:
        return 1
    if n <= 2:
        return n
    result=[1,2]
    for i in range(n-2):
        result.append(result[-2]+result[-1])
    return result[-1]

  def minimumTotal(self, triangle):
    n, m = len(triangle), len(triangle[-1])
    path_sum = triangle[-1]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            path_sum[j] = min(path_sum[j], path_sum[j + 1]) + triangle[i][j]

    return path_sum[0]

  def minimumTotal2(self, t):
    n = len(t)
    for i in range(n):
      for j in range(i+1):
        if i == 0 and j == 0:
          continue
        elif j == 0:
          t[i][j] += t[i - 1][j]
        elif j == i:
          t[i][j] += t[i - 1][j - 1]
        else:
          t[i][j] += min(t[i - 1][j], t[i - 1][j - 1]);
    return min(t[-1])

  #Dp[i] 表示以第i个数字为结尾的最长上升子序列的长度。
  #对于每个数字，枚举前面所有小于自己的数字 j
  #Dp[i] = max{Dp[j]} + 1. 如果没有比自己小的，Dp[i] = 1;
  def longestIncreasingSubsequenceNsquare(self, nums):
    n = len(nums)
    dp = [1] * n
    for i in range(n):
      for j in range(i):
        if nums[j] < nums[i] and dp[i] <= dp[j]:
          dp[i] = dp[j] + 1
    return max(dp)
  # B[i]存储Dp值为i的最小的数字。（有多个位置，以这些位置为结尾的LIS长度都为i， 则这些数字中最小的一个存在B[i]中）
  # 则B数组严格递增。且下标表示LIS长度，也是严格递增，可以在B数组中进行二分查找。
  # 对于每个位置i，我们要找，所有小于A[i], 且Dp值最大的那个。这个操作在B数组中二分查找
  def longestIncreasingSubsequenceNsquare2(self, nums):
    n = len(nums)
    dp = [1] * n
    B = [math.inf] * (n+1)
    B[1] = nums[0]

    for i in range(1, n):
      for j in range(1, n+1):
        if B[j] < nums[i]:
          dp[i] = j + 1
          B[j + 1] = min(nums[i],B[j + 1])
      B[1] = min(nums[i],B[1])
    return max(dp)
  # import bisect
  def longestIncreasingSubsequenceBi(self, nums) -> int:
    if not nums: return 0
    subsequence = [nums[0]]

    for num in nums[1:]:
      if num > subsequence[-1]:
          subsequence.append(num)
      elif num < subsequence[-1]:
          # overide_index = bisect.bisect(subsequence, num)
          overide_index = self.bisect(subsequence, num)
          subsequence[overide_index] = num
    return len(subsequence)
  # return a num equal or larger than target
  def bisect(self,a, target):
    lo = 0
    hi = len(a) - 1
    while lo + 1 < hi:
      mid = (lo + hi) // 2
      if a[mid] > target:
        hi = mid
      elif a[mid] < target:
        lo = mid + 1
      else:
        return mid
    if a[lo] == target:
      return lo
    if a[hi] == target:
      return hi
    if a[lo] > target:
      return lo
    return hi

  # @param {int[]} nums a set of distinct positive integers
  # @return {int[]} the largest subset
  def largestDivisibleSubset(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # write your code here
    if len(nums) < 2:
        return nums
    # record the index of the previous divisible number
    prev_index = [-1] * len(nums)

    # record how many divisible numbers so far
    counts = [1]*len(nums)

    # sort the arrray as the counts needs to be increasing
    nums.sort()

    for i in range(1, len(nums)):
        for j in range(i):
            # update counts only if the counts can be higher
            if nums[i] % nums[j] == 0 and counts[j] + 1 > counts[i]:
                counts[i] = counts[j] + 1
                prev_index[i] = j

    # find the element with the most counts
    # then get the result array with the previous number indicies in a loop.
    index = counts.index(max(counts))
    res = []
    while index != -1:
        res.append(nums[index])
        index = prev_index[index]
    return res[::-1]

  def canJumpGreedy(self, A):
    max_so_far = 0
    for i in range(len(A)):
      if max_so_far < i:
        return False
      max_so_far = max(max_so_far, A[i] + i)
    return True

  def canJumpDP(self, A):
    l = len(A)
    dp = [1] + [0]*(l-1)
    for i in range(l):
      if dp[i] is 0:
        continue
      for j in range(A[i]):
        if i+j+1 < l:
            dp[i+j+1] = 1
    return dp[-1] == 1



root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right = Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)
root.right.right.right.right.right = Node(10)
# 28
m = 10
A = [1, 2, 4, 2, 5]
V = [5, 3, 5, 3, 2]
sol = Solution()
# print(sol.backPackII(m, A, V))
grid = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
nums = [1,2,4,6, 7, 8]
longest = [5,1,3,6,5,7]
longest1 = [10,1,11,2,12,3,11]
a = [3,2,1,0,4]
a1 = [2,3,1,1,4]
print(sol.canJumpDP(a))
print(sol.canJumpDP(a1))


