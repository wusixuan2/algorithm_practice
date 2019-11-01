class Node:
    def __init__(self, value, left=None, right=None):
        self.left =left
        self.val = value
        self.right = right
    def __str__(self):
        return str(self.val)

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#     def create(self, val):
#         if self.root == None:
#             self.root = Node(val)
#         else:
#             current = self.root

#             while True:
#                 if val < current.info:
#                     if current.left:
#                         current = current.left
#                         # print("move to left node")
#                         # print(current)
#                     else:
#                         current.left = Node(val)
#                         # print("make a left node")
#                         # print(current)
#                         # print(current.left)
#                         break
#                 elif val > current.info:
#                     if current.right:
#                         current = current.right
#                         # print("move to right node")
#                         # print(current)
#                     else:
#                         current.right = Node(val)
#                         # print("make a right node")
#                         # print(current)
#                         # print(current.right)
#                         break
#                 else:
#                     break
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.val)
#         inorder(root.right)

# def preorder(root):
#     if root:
#         print(root.val)
#         preorder(root.left)
#         preorder(root.right)

# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.val)

# def total_nodes(root):
#     if (not root):
#         return 0
#     else :
#         return 1+total_nodes(root.left)+total_nodes(root.right)

# def height(root):
#   if (not root):
#     return -1
#   else:
#     return max(height(root.left) + 1, height(root.right) + 1)

# input1 = "7 3 5 2 1 4 6 7"
# input = "6 4 2 3 1 7 6"

# tree = BinarySearchTree()
# t = int(input[0])

# arr = list(map(int, input[2:].split()))

# for i in range(t):
#     tree.create(arr[i])

# root1 = Node(1)
# root2 = Node(1)

# root1.left = Node(2)
# root1.right = Node(3)
# root1.left.left = Node(4)
# root1.left.right = Node(5)

# root2.left = Node(3)
# root2.right = Node(2)
# root2.right.left = Node(5)
# root2.right.right = Node(4)

# def inorder_arr(root, arr):
#     if root:
#         inorder_arr(root.left, arr)
#         arr.append(root.info)
#         inorder_arr(root.right, arr)

# def isMirror(root1, root2):
#   arr1 = []
#   arr2 = []
#   inorder_arr(root1, arr1)
#   inorder_arr(root2, arr2)
#   print(arr1, arr2)
#   return arr1[::-1] == arr2

# def areMirror(a, b):

#     # Base case : Both empty
#     if a is None and b is None:
#         return True

#     # If only one is empty
#     if a is None or b is None:
#         return False

#     # Both non-empty, compare them
#     # recursively. Note that in
#     # recursive calls, we pass left
#     # of one tree and right of other tree
#     return (a.data == b.data and
#             areMirror(a.left, b.right) and
#             areMirror(a.right , b.left))
# # print(isMirror(root1, root2))

# def lca(root, n1, n2):
#   # Base Case
#     if root is None:
#         return None

#     # If both n1 and n2 are smaller than root, then LCA
#     # lies in left
#     if(root.info > n1 and root.info > n2):
#         return lca(root.left, n1, n2)

#     # If both n1 and n2 are greater than root, then LCA
#     # lies in right
#     if(root.info < n1 and root.info < n2):
#         return lca(root.right, n1, n2)

#     return root
# # print(lca(tree.root, 1, 7))


# # def preorder(root, arr):
# #     if root:
# #         arr.append(root.info)
# #         preorder(root.left, arr)
# #         preorder(root.right, arr)


# def isBST(root):
#   ans = []
#   inorder_arr(root, ans)

#   sorted = ans[:]
#   sorted.sort()
#   return sorted == ans

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(1)
root.right.right.left = Node(5)

def rob_brute(node):
  if (node == None):
    return 0
  if (node.left == None and node.right == None):
    return node.val
  if (node.left != None and node.right != None):
    return max(node.val + rob_brute(node.left.left),
      node.val + rob_brute(node.left.right),
      node.val + rob_brute(node.right.left),
      node.val + rob_brute(node.right.right),
      rob_brute(node.left),
      rob_brute(node.right))
  if (node.right == None):
    return max(node.val + rob_brute(node.left.left),
      node.val + rob_brute(node.left.right),
      rob_brute(node.left))
  if (node.left == None):
    return max(
      node.val + rob_brute(node.right.left),
      node.val + rob_brute(node.right.right),
      rob_brute(node.right))

def rob(root):
  rob, not_rob = visit(root)
  return max(rob, not_rob)

def visit(root):
  if root is None:
    return 0, 0

  left_rob, left_not_rob = visit(root.left)
  # print(left_rob, left_not_rob)
  right_rob, right_not_rob = visit(root.right)
  # print(right_rob, right_not_rob)

  rob = root.val + left_not_rob + right_not_rob
  not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
  # print(rob, not_rob)
  return rob, not_rob

print(rob_brute(root))
print(rob(root))


