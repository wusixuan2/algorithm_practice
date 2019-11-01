def twoSum(self, nums, target):
    dict = {}
    for i in range(len(nums)):
        if target-nums[i] not in dict:
            dict[nums[i]]=i
        else:
            return [dict[target-nums[i]],i]

def find3Numbers(A, sum):
    arr_size = len(A)
    for i in range(0, arr_size-1):
        # Find pair in subarray A[i + 1..n-1]
        # with sum equal to sum - A[i]
        s = set()
        curr_sum = sum - A[i]
        for j in range(i + 1, arr_size):
            if (curr_sum - A[j]) in s:
                return [A[i], curr_sum-A[j], A[j]]
            s.add(A[j])

    return False

A = [4, 1, 45, 6, 10, 8]
sum = 22

print(find3Numbers(A, sum))

