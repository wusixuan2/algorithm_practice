class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    #dp sulution
    def maxSubArray(self, nums):
        if len(nums) == 0: return 0
        dp = [0 for x in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i-1]) + nums[i]
        max_value = -sys.maxsize - 1
        for v in dp:
            max_value = max(max_value, v)
        return max_value

    #prefix sum Solution
    def maxSubArray(self, nums):
        if len(nums) == 0: return 0
        prefix_sum = 0
        min_sum = 0
        max_slice = -sys.maxsize - 1
        for n in nums:
            prefix_sum += n
            max_slice = max(max_slice, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)
        return max_slice

    #greedy
    def maxSubArray(self, nums):
        if len(nums) == 0: return 0
        sum = 0
        slice = -sys.maxsize - 1
        for n in nums:
            sum += n
            slice = max(slice, sum)
            sum = max(0, sum)
        return slice

    # find two non-overlapping subarrays which have the largest sum
    # left[i] 代表从最左边到 i 位置所能取得的最大 subarray sum;
    # right[i] 代表从最右边到 i 位置所能取得的最大 subarray sum;
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        if not nums:
            return 0

        n = len(nums)
        left = [0] * n
        right = [0] * n

        left[0] = nums[0]
        max_so_far = nums[0]
        max_ending_here = nums[0]
        for i in range(1, n):
            max_ending_here = max(nums[i], nums[i] + max_ending_here)
            max_so_far = max(max_so_far, max_ending_here)

            left[i] = max_so_far


        right[n - 1] = nums[n - 1]
        max_so_far = nums[n - 1]
        max_ending_here = nums[n - 1]
        for i in range(n - 2, -1, -1):
            max_ending_here = max(nums[i], nums[i] + max_ending_here)
            max_so_far = max(max_so_far, max_ending_here)

            right[i] = max_so_far

        res = -sys.maxint - 1
        for i in range(n - 1):
            res = max(res, left[i] + right[i + 1])
        return res

    # Given an array of integers and a number k, find k non-overlapping subarrays which have the largest sum.
    # 1.确定状态：
    # dp[i][j] 为前i个数可取，子数组数量为j 的解
    # A[i - 1] 为当前待取的值

    # 2.转移方程：
    # dp[i][j] = max( dp[i - 1][j], dp[i - 1][j - 1] + A[i - 1], dp[i - 1][j] + A[i - 1] )
    # 分别为不取当前值；前i - 1个数取j - 1 个子数组的情况下 当前值组成单独的子数组； 前i - 1个数取好了j 个数组 当前值加到最后一个子数组中
    # 但是这里最后一种情况有一个必要条件： 前一个数必须取的情况下，当前的数才能加入到最后一个子数组。
    # A = [-1, 4, -2，3] k = 1 的情况: dp[3][1] + A[3] = 4 + 3 = 7 但是这里是不能转化到 dp[4][1] 的
    # 所以这里需要两个list:
    # dp1 为取当前值的状态 ,dp2 为不取当前值的状态。
    # dp1[i][j] = max(dp1[i - 1][j] + A[i - 1], dp1[i - 1][j - 1] + A[i - 1], dp2[i - 1][j - 1] + A[i - 1])
    # dp2[i][j] = max(dp1[i - 1][j], dp2[i - 1][j])

    # 3.初始条件和边界情况：
    # j == 0 : dp[i][0] = 0 取0个子数组
    # j > i : 子数组数量超过了数组长度，无解

    # 4.计算顺序：
    # top down & left to right

    def maxSubArray(self, nums, k):
        m = len(nums)
        MIN = (1 << 31) * -1

        #dp1 为取当前数的状态 dp2 为不取当前数的状态
        #初始化
        dp1 = [[MIN for _ in range(k + 1)] for _ in range(m + 1)]
        dp2 = [[MIN for _ in range(k + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            dp1[i][0] = 0 # 子数组数目为0，解为0
            dp2[i][0] = 0
            for j in range(1, min(i + 1, k + 1)):#子数组数目不能超过i（当前可取的数的数目） 和 k 的最小值
                dp1[i][j] = max(dp1[i - 1][j] + nums[i - 1], dp1[i - 1][j - 1] + nums[i - 1], dp2[i - 1][j - 1] + nums[i - 1])
                #因为不能跳着取数 从dp[i - 1][j] + nums[i - 1] 转化到 dp[i][j]的必要条件是取了上一个数，所以 必须从dp1 表转换
                #从 dp[i - 1][j - 1] + nums[i - 1] 转化则没有限制上一个数是否取

                dp2[i][j] = max(dp1[i - 1][j], dp2[i - 1][j])
                #比较上个数取和不取的情况

        return max(dp1[m][k] ,dp2[m][k])
