from collections import deque

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
# print(shortestPath(grid2, source, destination))

################ graph find route ################
graph1 = {
          0: [1, 2, 3],
          1: [4],
          2: [4, 5],
          3: [4,5],
          4: [],
          5: [6],
          6:[]
          }

def find_route(graph, orig, dest, visited):
  if orig == dest: return [orig]

  nbrs = find_neigbor(orig, graph)
  visited.append(orig)
  route = dfs(graph, nbrs, dest, visited)

  if not route: return False

  route.insert(0, orig)
  return route

def dfs(graph, nbrs, dest, visited):
  if not nbrs: return False
  if nbrs[0] in visited:
    return dfs(graph, nbrs[1:], dest, visited)
  route = find_route(graph, nbrs[0], dest, visited)
  if not route:
    return dfs(graph, nbrs[1:], dest, visited)
  else:
    return route

def find_neigbor(node, graph):
  if node not in graph:
    return False
  return graph[node]

# print(find_route(graph1, 0, 6, []))
################ Sequence Reconstruction ################
class Solution:
    def sequenceReconstruction(self, org, seqs):
        graph = self.build_graph(seqs)
        topo_order = self.topological_sort(graph)
        return topo_order == org

    def build_graph(self, seqs):
        # initialize graph
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()

        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])

        return graph

    def get_indegrees(self, graph):
        indegrees = {
            node: 0
            for node in graph
        }

        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1

        return indegrees

    def topological_sort(self, graph):
        indegrees = self.get_indegrees(graph)

        queue = []
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)

        topo_order = []
        while queue:
            if len(queue) > 1:
                # there must exist more than one topo orders
                return None

            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) == len(graph):
            return topo_order

        return None

org1 = [1,2,3]
seqs1 = [[1,2],[1,3],[2,3]]
org2 = [4,1,5,2,6,3]
seqs2 = [[5,2,6,3],[4,1,5,2]]
org3 = [1,2,3]
seqs3 = [[1,2],[1,3]]
# print(sequenceReconstruction(org1, seqs1))
################ Serialize and Deserialize Binary Tree ################
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.left =left
        self.val = value
        self.right = right
    def __str__(self):
        return str(self.val)
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.right = Node(3)
# root.right.left = Node(4)
# root.right.right = Node(1)
# root.right.right.left = Node(5)
class Solution1:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        if root is None:
            return ""

        # use bfs to serialize the tree
        queue = deque([root])
        bfs_order = []
        while queue:
            node = queue.popleft()
            bfs_order.append(str(node.val) if node else '#')
            if node:
                queue.append(node.left)
                queue.append(node.right)

        return ' '.join(bfs_order)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    def deserialize(self, data):
        # None or ""
        if not data:
            return None

        bfs_order = [
            TreeNode(int(val)) if val != '#' else None
            for val in data.split()
        ]
        root = bfs_order[0]
        fast_index = 1

        nodes, slow_index = [root], 0
        while slow_index < len(nodes):
            print("slow node",slow_index, len(nodes),fast_index)
            node = nodes[slow_index]
            slow_index += 1
            node.left = bfs_order[fast_index]
            node.right = bfs_order[fast_index + 1]
            fast_index += 2

            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return root

sol = Solution1()
# print(sol.serialize(root))
# print(sol.deserialize("1 2 3 # 3 4 1 # # # # 5 # # #"))
################ Clone Graph ################
class Solution:
    def cloneGraph(self, node):
        root = node
        if node is None:
            return node

        # use bfs algorithm to traverse the graph and get all nodes.
        nodes = self.getNodes(node)

        # copy nodes, store the old->new mapping information in a hash map
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)

        # copy neighbors(edges)
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    def getNodes(self, node):
        q = collections.deque([node])
        result = set([node])
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    q.append(neighbor)
        return result
################ word ladder ################
import collections
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.append(end)
        queue = collections.deque([start])
        visited = set([start])

        distance = 0
        while queue:
            distance += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance

                for next_word in self.get_next_words(word):
                    if next_word not in dict or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)

        return 0

    # O(26 * L^2)
    # L is the length of word
    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words

sol = Solution()
start = "a"
end = "c"
dict =["a","b","c"]
start ="hit"
end = "cog"
dict =["hot","dot","dog","lot","log"]
print(sol.ladderLength(start, end, dict))



