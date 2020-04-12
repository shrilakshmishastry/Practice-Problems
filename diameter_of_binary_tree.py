# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path
# between any two nodes in a tree. This path may or may not pass through the root. 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
    def dfs(self, node):
        if not node:
             return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.ans =max(self.ans,right+left)
        return max(left+1,right+1)
