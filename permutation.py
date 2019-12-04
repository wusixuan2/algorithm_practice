class Solution:
    # 从最后一个位置开始，找到一个上升点，上升点之前的无需改动。
    # 然后，翻转上升点之后的降序。
    # 在降序里，找到第一个比上升点大的，交换位置。
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutationI(self, num):
        for i in range(len(num)-2, -1, -1):
            if num[i] < num[i+1]:
                break
        else:
            num.reverse()
            return num
        for j in range(len(num)-1, i, -1):
            if num[j] > num[i]:
                num[i], num[j] = num[j], num[i]
                break
        for j in range(0, (len(num) - i)//2):
            num[i+j+1], num[len(num)-j-1] = num[len(num)-j-1], num[i+j+1]
        return num

    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        # 倒序遍历
        for i in range(len(nums)-1, -1, -1):
            # 找到第一个数值变小的点，这样代表右边有大的可以和它换，而且可以保证是next permutation
            if i > 0 and nums[i] > nums[i-1]:
                # 找到后再次倒序遍历，找到第一个比刚才那个数值大的点，互相交换
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        # 因为之前保证了，右边这段数从右到左是一直变大的，所以直接双指针reverse
                        left, right = i, len(nums)-1
                        while left <= right:
                            nums[left], nums[right] = nums[right], nums[left]
                            left += 1
                            right -= 1
                        return nums
        # 如果循环结束了，表示没找到能替换的数，表示序列已经是最大的了
        nums.reverse()
        return nums

    def nextPermutation(self, nums):
        # write your code here
        #corner case 1
        if len(nums) <= 1:
            return

        #find the exchange pos
        target_pos = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                target_pos = i
                break

        #corner case 2 -> juse reverse
        #important 记住还要满足nums[0] >= nums[1] 这个条件 不然会出现类似[2,1,3]这样的情况！
        if target_pos == 0 and nums[0] >= nums[1]:
            nums.reverse()
            return

        #find the 1st larget than the value of target_pos
        first_larger_pos = len(nums) - 1
        for i in range(len(nums) - 1, target_pos, -1):
            if nums[i] > nums[target_pos]:
                first_larger_pos = i
                break

        nums[target_pos], nums[first_larger_pos] = nums[first_larger_pos], nums[target_pos]
        #reverse
        left, right = target_pos + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
