class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

import sys
class Solution:
    def closestValue(self, root, target):
        upper = root
        lower = root
        while root:
            if target > root.val:
                lower = root
                root = root.right
            elif target < root.val:
                upper = root
                root = root.left
            else:
                return root.val
        if abs(upper.val - target) <= abs(lower.val - target):
            return upper.val
        return lower.val

    #######
    def findSubtree(self, root):
        self.minumum_weight = sys.maxsize
        self.subtree = None
        self.helper(root)

        return self.subtree

    def helper(self, root):
        if root is None:
            return 0

        left_weight = self.helper(root.left)
        right_weight = self.helper(root.right)
        root_weight = left_weight + right_weight + root.val

        if root_weight < self.minumum_weight:
            self.minumum_weight = root_weight
            self.subtree = root

        return root_weight

    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        balanced, _ = self.validate(root)
        return balanced

    def validate(self, root):
        if root is None:
            return True, 0

        balanced, leftHeight = self.validate(root.left)
        if not balanced:
            return False, 0
        balanced, rightHeight = self.validate(root.right)
        if not balanced:
            return False, 0

        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1

    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        self.lastVal = None
        self.isBST = True
        self.validate(root)
        return self.isBST

    # inorder
    def validate(self, root):
        if root is None: return
        self.validate(root.left)
        if self.lastVal is not None and self.lastVal >= root.val:
            self.isBST = False
            return
        self.lastVal = root.val
        self.validate(root.right)

    def preorder(self, root):
      if root:
          print(root.val)
          self.preorder(root.left)
          self.preorder(root.right)
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversalMorrisQueue(self, root):
        stack = []
        preorder = []

        if not root:
            return preorder

        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return preorder
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversalMorris(self, root):
        nums = []
        cur = None

        while root:
            if root.left:
                cur = root.left
                while cur.right and cur.right != root:
                    cur = cur.right
                if cur.right == root:
                    cur.right = None
                    root = root.right
                else:
                    nums.append(root.val)
                    cur.right = root
                    root = root.left
            else:
                nums.append(root.val)
                root = root.right

        return nums


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(7)
root.right.right.left = Node(6)
sol = Solution()
print(sol.preorderTraversalMorrisQueue(root))
print(sol.preorderTraversalMorris(root))
print(sol.preorder(root))

