# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence
# of nodes from some starting node to any node in the
# tree along the parent-child connections.
# The path must contain at least one node and does not
# need to go through the root.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = float('-inf')

        def dfs(root):
            if root == None:
                return 0
            left_max = max(0,dfs(root.left))
            right_max = max(0,dfs(root.right))
            self.max = max(self.max,right_max+left_max+root.val)
            return max(left_max,right_max)+root.val
        dfs(root)
        return self.max
