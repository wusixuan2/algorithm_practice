# Input:
#   [ [3,0,8,4],
#     [2,4,5,7],
#     [9,2,6,3],
#     [0,3,1,0] ]
# Output: 35
# Explanation:
#   The skyline viewed from north or south is: [9, 4, 8, 7]
#   The skyline viewed from west or right is: [8, 7, 9, 3]
#   The grid after increasing the height of buildings without affecting skylines is:
#   [ [8,4,8,7],
#     [7,4,7,7],
#     [9,4,8,7],
#     [3,3,3,3] ]
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])

        sum_ = 0

        for i in range(row):
            max_i = max(grid[i])
            for j in range(col):
                max_j = max([row[j] for row in grid])
                maximum = min(max_i, max_j)
                if grid[i][j] < maximum:
                    sum_ += maximum-grid[i][j]

        return sum_

########################### Merge k Sorted Arrays ###########################
import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        result = []
        heap = []
        for index, array in enumerate(arrays):
            if len(array) == 0:
                continue
            heapq.heappush(heap, (array[0], index, 0))

        while len(heap):
            val, x, y = heap[0]
            heapq.heappop(heap)
            result.append(val)
            if y + 1 < len(arrays[x]):
                heapq.heappush(heap, (arrays[x][y + 1], x, y + 1))

        return result

    # 自顶向下的分治法
    def mergekSortedArrays(self, arrays):
        return self.merge_range_arrays(arrays, 0, len(arrays) - 1)

    def merge_range_arrays(self, arrays, start, end):
        if start == end:
            return arrays[start]

        mid = (start + end) // 2
        left = self.merge_range_arrays(arrays, start, mid)
        right = self.merge_range_arrays(arrays, mid + 1, end)
        return self.merge_two_arrays(left, right)

    def merge_two_arrays(self, arr1, arr2):
        i, j = 0, 0
        array = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                array.append(arr1[i])
                i += 1
            else:
                array.append(arr2[j])
                j += 1
        while i < len(arr1):
            array.append(arr1[i])
            i += 1
        while j < len(arr2):
            array.append(arr2[j])
            j += 1
        return array

    # 自底向上两两归并
    def mergekSortedArrays(self, arrays):
        while len(arrays) > 1:
            next_arrays = []
            for i in range(0, len(arrays), 2):
                if i + 1 < len(arrays):
                    array = self.merge_two_arrays(arrays[i], arrays[i + 1])
                else:
                    array = arrays[i]
                next_arrays.append(array)
            arrays = next_arrays

        return arrays[0]

    def merge_two_arrays(self, arr1, arr2):
        i, j = 0, 0
        array = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                array.append(arr1[i])
                i += 1
            else:
                array.append(arr2[j])
                j += 1
        while i < len(arr1):
            array.append(arr1[i])
            i += 1
        while j < len(arr2):
            array.append(arr2[j])
            j += 1
        return array

