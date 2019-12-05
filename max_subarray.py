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
