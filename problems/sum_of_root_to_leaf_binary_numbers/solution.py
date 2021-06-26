# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode, s=0) -> int:
        if not root:
            return 0
        s = s *2 + root.val
        if root.left or root.right:
            return self.sumRootToLeaf(root.left, s) + self.sumRootToLeaf(root.right, s)
        else:
            return s
        
        