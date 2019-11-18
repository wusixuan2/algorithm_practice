import math
import sys
def twoSum(a, target):
  dictNum = dict()
  for i in range(len(a)):
    if (a[i] in dictNum):
      return dictNum[a[i]], i

    dictNum[target - a[i]]= i
  return -1

def threeSum(a, target):
  for i in range(len(a)-2):
    dictNum = dict()
    for j in range(i+1, len(a)):
      print(i,j, dictNum)
      if (a[j] in dictNum):
        return i, dictNum[a[j]], j
      dictNum[target - a[i] - a[j]]= j
  return -1

def twoDiff(a, target):
  hashmap = dict()
  for i in range(len(a)):
    if (a[i] in hashmap):
      return hashmap[a[i]], i
    hashmap[a[i] - target]= i
    hashmap[a[i] + target]= i
  return -1
def twoSquareDiff(a, target):
  hashmap = dict()
  for i in range(len(a)):
    if (a[i] in hashmap):
      return hashmap[a[i]], i
    hashmap[math.sqrt(abs(a[i]*a[i] - target))]= i
    hashmap[math.sqrt(a[i]*a[i] + target)]= i
  return -1

# 每个位置上的盛水数目 = min(左侧最高，右侧最高) - 当前高度
# 从左到右扫描一边数组，获得每个位置往左这一段的最大值，再从右到左扫描一次获得每个位置向右的最大值。
# 然后最后再扫描一次数组，计算每个位置上的盛水数目。
# 时间复杂度 O(n)O(n)，空间复杂度 O(n)O(n)
def trapRainWater(heights):
  if not heights:
      return 0

  left_max = []
  curt_max = -sys.maxsize
  for height in heights:
      curt_max = max(curt_max, height)
      left_max.append(curt_max)

  right_max = []
  curt_max = -sys.maxsize
  for height in reversed(heights):
      curt_max = max(curt_max, height)
      right_max.append(curt_max)

  right_max = right_max[::-1]

  water = 0
  n = len(heights)
  for i in range(n):
      water += (min(left_max[i], right_max[i]) - heights[i])
  return water

from heapq import heappush, heappop
"""
@param heights: a matrix of integers
@return: an integer
"""
def trapRainWater2d(heights):
    if not heights:
        return 0
    row, col = len(heights), len(heights[0])
    hq = []
    visited = set([])
    for r in range(row):
        heappush(hq, (heights[r][0], r, 0))
        visited.add((r, 0))
        heappush(hq, (heights[r][col-1], r, col-1))
        visited.add((r, col-1))
    for c in range(col):
        heappush(hq, (heights[0][c], 0, c))
        visited.add((0, c))
        heappush(hq, (heights[row-1][c], row-1, c))
        visited.add((row-1, c))
    water = 0
    while hq:
        height, old_r, old_c = heappop(hq)
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            new_r, new_c = old_r + dr, old_c + dc
            if not (0 <= new_r <= row-1 and 0 <= new_c <= col-1):
                continue
            if (new_r, new_c) in visited:
                continue
            visited.add((new_r, new_c))
            water += max(0, height - heights[new_r][new_c])
            heappush(hq, (max(height, heights[new_r][new_c]), new_r, new_c))
    return water
heights = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(trapRainWater(heights)) # 6
heights2d = [[12,13,0,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
print(trapRainWater2d(heights2d)) # 14


