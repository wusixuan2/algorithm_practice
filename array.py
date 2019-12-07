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
