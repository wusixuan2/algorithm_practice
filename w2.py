class Node:
    def __init__(self, value, left=None, right=None):
        self.left =left
        self.val = value
        self.right = right
    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def create(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            current = self.root

            while True:
                if value < current.val:
                    if current.left:
                        current = current.left
                        # print("move to left node")
                        # print(current)
                    else:
                        current.left = Node(value)
                        # print("make a left node")
                        # print(current)
                        # print(current.left)
                        break
                elif value > current.val:
                    if current.right:
                        current = current.right
                        # print("move to right node")
                        # print(current)
                    else:
                        current.right = Node(value)
                        # print("make a right node")
                        # print(current)
                        # print(current.right)
                        break
                else:
                    break
root1 = Node(1)
root2 = Node(1)

root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2.left = Node(3)
root2.right = Node(2)
root2.right.left = Node(5)
root2.right.right = Node(4)

grid1 = [
  [1,1,1,1,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
from collections import deque

############################## Number of islands ##############################
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslandsBFS(self, grid):
        if not grid or not grid[0]:
            return 0
        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1

        return islands

    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:

          x, y = queue.popleft()
          for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
              next_x = x + delta_x
              next_y = y + delta_y
              if self.is_valid(grid, next_x, next_y, visited):
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y]

    """
      :type grid: List[List[str]]
      :rtype: int
    """
    def numlandDFS(self, grid):

        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])

        ans = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    ans += 1
                    self.__dfs(grid, x, y, n, m)
        return ans

    def __dfs(self, grid, x, y, n, m):
        if x < 0 or y < 0 or x >=n or y >= m or grid[y][x] == 0:
            return
        grid[y][x] = 0
        self.__dfs(grid, x + 1, y, n, m)
        self.__dfs(grid, x - 1, y, n, m)
        self.__dfs(grid, x, y + 1, n, m)
        self.__dfs(grid, x, y - 1, n, m)

sol = Solution()
print(sol.numIslandsBFS(grid1))

class MyQueue:
    # 队列初始化
    def __init__(self):
        self.elements = []  # 用list存储队列元素
        self.pointer = 0    # 队头位置

    # 获取队列中元素个数
    def size(self):
        return len(self.elements)-pointer

    # 判断队列是否为空
    def empty(self):
        return self.size() == 0

    # 在队尾添加一个元素
    def add(self, e):
        self.elements.append(e)

    # 弹出队首元素，如果为空则返回None
    def poll(self):
        if self.empty():
            return None
        pointer += 1
        return self.elements[pointer-1]

from collections import deque

queue = deque()
seen = set()
# 无需分层遍历的宽度优先搜索
# seen.add(start)
# queue.append(start)
# while len(queue):
#     head = queue.popleft()
#     for neighbor in head.neighbors:
#         if neighbor not in seen:
#             seen.add(neighbor)
#             queue.append(neighbor)


#需要分层遍历的宽度搜先搜索

# seen.add(start)
# queue.append(start)
# while len(queue):
#     size = len(queue)
#     for _ in range(size):
#         head = queue.popleft()
#         for neighbor in head.neighbors:
#             if neighbor not in seen:
#                 seen.add(neighbor)
#                 queue.append(neighbor)

# 使用两个队列的BFS实现

# seen.add(start)
# queue1.append(start)
# currentLevel = 0
# while len(queue1):
#     size = len(queue1)
#     for _ in range(size):
#         head = queue1.popleft()
#         for neighbor in head.neighbors:
#             if neighbor not in seen:
#                 seen.add(neighbor)
#                 queue2.append(neighbor)
#     queue1, queue2 = queue2, queue1
#     queue2.clear()
#     currentLevel += 1


############################## Binary tree level order traversal ##############################
from collections import deque

class Solution1:
    def levelOrder(self, root):
        if root is None:
            return []

        queue = deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft() # dont do pop(0), will shift
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
# sol = Solution1()
# print(sol.levelOrder(root1))



############################################################



from collections import deque


class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {boolean} true if can finish all courses or false
    def canFinish(self, numCourses, prerequisites):
        # Write your code here
        edges = {i: [] for i in range(numCourses)}
        degrees = [0 for i in range(numCourses)]
        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1

        queue, count = deque([]), 0

        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            count += 1

            for x in edges[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    queue.append(x)

        return count == numCourses


prerequisites1 = [[4,0],[4,1],[3,1],[3,2],[5,4],[5,3]]
numCourses1 = 6
prerequisites2 = [[5,8],[3,5],[1,9],[1,9],[4,5],[0,2],[7,8],[4,9]]
numCourses2 = 10
from collections import deque

def canFinish(numCourses, prerequisites):
  graph = {} # store requisite as key and course require that requisite as value
  inDegree = [0] * numCourses #限制
  for i in prerequisites:
    toTake = i[0]
    preReq = i[1]
    inDegree[toTake] += 1
    if preReq in graph:
      graph[preReq].append(toTake)
    else:
      graph[preReq] = [toTake]
  queue = deque([])
  for i in range(len(inDegree)):
    if inDegree[i] == 0:
      queue.append(i)
  while queue:
    preReq = queue.popleft()
    if (preReq in graph):
      toTakeList = graph[preReq]
      for toTake in toTakeList:
        inDegree[toTake] -= 1
        if (inDegree[toTake] == 0):
          queue.append(toTake)
  for i in range(len(inDegree)):
    if inDegree[i] != 0: return False
  return True



from collections import deque

################ Course Schedule II ###############
def findOrder(numCourses, prerequisites):
  graph = {} # store requisite as key and course require that requisite as value
  inDegree = [0] * numCourses #限制
  for i in prerequisites:
    toTake = i[0]
    preReq = i[1]
    inDegree[toTake] += 1
    if preReq in graph:
      graph[preReq].append(toTake)
    else:
      graph[preReq] = [toTake]
  queue = deque([])
  ans = []
  for i in range(len(inDegree)):
    if inDegree[i] == 0:
      queue.append(i)

  while queue:
    preReq = queue.popleft()
    ans.append(preReq)

    if (preReq in graph):
      toTakeList = graph[preReq]
      for toTake in toTakeList:
        inDegree[toTake] -= 1
        if (inDegree[toTake] == 0):
          queue.append(toTake)
  return ans

################ Knight Shortest Path ################
DIRECTIONS = [
    (-2, -1), (-2, 1), (-1, 2), (1, 2),
    (2, 1), (2, -1), (1, -2), (-1, -2),
]
def shortestPath(grid, source, destination):
  queue = deque([(source[0], source[1])])
  distance = {(source[0], source[1]): 0}

  while queue:
    x, y = queue.popleft()
    if (x, y) == (destination[0], destination[1]):
      return distance[(x, y)]
    for dx, dy in DIRECTIONS:
      next_x, next_y = x + dx, y + dy
      if (next_x, next_y) in distance:
          continue
      if not is_valid(next_x, next_y, grid):
          continue
      distance[(next_x, next_y)] = distance[(x, y)] + 1
      queue.append((next_x, next_y))
  return -1

def is_valid(x, y, grid):
  n, m = len(grid), len(grid[0])

  if x < 0 or x >= n or y < 0 or y >= m:
      return False

  return not grid[x][y]

grid1 = [[0,0,0],
 [0,0,0],
 [0,0,0]]
grid2 = [[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0]
destination = [2, 2]
print(shortestPath(grid2, source, destination))


