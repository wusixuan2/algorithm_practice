class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def lastPosition(self, A, target):
        if not A or target is None:
            return -1

        start = 0
        end = len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2

            if A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid

        if A[end] == target:
            return end
        elif A[start] == target:
            return start
        else:
            return -1
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        if not nums:
            return -1

        # find first index i so that nums[i] > nums[i + 1]
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # mid + 1 保证不会越界
            # 因为 start 和 end 是 start + 1 < end
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid

        return max(nums[start], nums[end])

    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        if n < 0 :
            x = 1 / x
            n = -n

        ans = 1
        tmp = x

        while n != 0:
            if n % 2 == 1:
                ans *= tmp
            tmp *= tmp
            n //= 2
        return ans

sol = Solution()
a1 = [1,2,3,4,4,6]
print(sol.lastPosition(a1, 4))
