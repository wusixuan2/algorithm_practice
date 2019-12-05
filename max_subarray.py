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
