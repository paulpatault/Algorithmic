"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.
"""


class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def universal_value(self, tree):
        pass # TODO


root = BinaryTree(0)
root.left = BinaryTree(1)
root.right = BinaryTree(0)
root.right.left = BinaryTree(1)
root.right.left.left = BinaryTree(1)
root.right.left.right = BinaryTree(1)
root.right.right = BinaryTree(0)

# print(root)

print(Solution().universal_value(root))
