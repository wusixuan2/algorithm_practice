class Solution:
    # @param head: the head of linked list.
    # @return: a middle node of the linked list
    def middleNode(self, head):
        if head is None:
            return None
        slow = head
        fast = slow.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                if left != right:
                    nums[left] = nums[right]
                left += 1
            right += 1

        while left < len(nums):
            if nums[left] != 0:
                nums[left] = 0
            left += 1

class TwoSum(object):

    def __init__(self):
        # initialize your data structure here
        self.count = {}


    # Add the number to an internal data structure.
    # @param number {int}
    # @return nothing
    def add(self, number):
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1



    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        for num in self.count:
            if value - num in self.count and \
                (value - num != num or self.count[num] > 1):
                return True
        return False
# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)

################################################################
# O(n) time, O(n) space
class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        d, result = {}, 0
        for num in nums:
            if num not in d:
                d[num] = True
                nums[result] = num
                result += 1

        return result

# O(nlogn) time, O(1) extra space
class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        nums.sort()
        result = 1
        for i in range(1, n):
            if nums[i - 1] != nums[i]:
                nums[result] = nums[i]
                result += 1

        return result

################################################################
class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        self.quickSort(A, 0, len(A) - 1)

    def quickSort(self, A, start, end):
        if start >= end:
            return

        left, right = start, end
        # key point 1: pivot is the value, not the index
        pivot = A[(start + end) / 2];

        # key point 2: every time you compare left & right, it should be
        # left <= right not left < right
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1

            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]

                left += 1
                right -= 1

        self.quickSort(A, start, right)
        self.quickSort(A, left, end)
################################################################
# Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        self.sort(colors, 1, k, 0, len(colors) - 1)

    def sort(self, colors, color_from, color_to, index_from, index_to):
        if color_from == color_to or index_from == index_to:
            return

        color = (color_from + color_to) // 2

        left, right = index_from, index_to
        while left <= right:
            while left <= right and colors[left] <= color:
                left += 1
            while left <= right and colors[right] > color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.sort(colors, color_from, color, index_from, right)
        self.sort(colors, color + 1, color_to, left, index_to)

    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left

    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if not A or k < 1 or k > len(A):
            return None
        return self.partition(A, 0, len(A) - 1, len(A) - k)

    def partition(self, nums, start, end, k):
        """
        During the process, it's guaranteed start <= k <= end
        """
        if start == end:
            return nums[k]

        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1

        # left is not bigger than right
        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)

        return nums[k]

