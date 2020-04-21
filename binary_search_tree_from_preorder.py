# Return the root node of a binary search tree that matches the given preorder traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder = sorted(preorder)
        return self.bstFromPreorderInorder(preorder,inorder)

    def bstFromPreorderInorder(self,preorder,inorder):
        preorderlen = len(preorder)
        inorderlen = len(inorder)

        if(inorder==None or preorder == None or preorderlen != inorderlen or preorderlen == 0):
            return None
        root = TreeNode(preorder[0])
        rootIndex = inorder.index(root.val)
        root.left = self.bstFromPreorderInorder(preorder[1:rootIndex+1],inorder[:rootIndex])
        root.right = self.bstFromPreorderInorder(preorder[rootIndex+1:],inorder[rootIndex+1:])
        return root
