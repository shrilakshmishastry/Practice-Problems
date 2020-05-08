# In a binary tree, the root node is at depth 0, 
# and children of each depth k node are at depth k+1.
#
# Two nodes of a binary tree are cousins
# if they have the same depth, but have different parents.
#
# We are given the root of a binary tree with unique values,
# and the values x and y of two different nodes in the tree.
#
# Return true if and only
#  if the nodes corresponding to the values x and y are cousins.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xInfo = []
        yInfo = []
        parent = None
        level = 0
        if root == None:
            return False
        self.dfs(root,level,parent,xInfo,yInfo,x,y)
        return xInfo[0]==yInfo[0] and xInfo[1]!=yInfo[1]


    def dfs(self,root,level,parent,xInfo,yInfo,x,y):
        if root is None:
            return None

        if root.val == x:
            xInfo.append(level)
            xInfo.append(parent)

        if  root.val ==y:
            yInfo.append(level)
            yInfo.append(parent)

        self.dfs(root.left,level+1,root,xInfo,yInfo,x,y)
        self.dfs(root.right,level+1,root,xInfo,yInfo,x,y)
