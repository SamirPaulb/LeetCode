# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        v = 0
        if(l != 0 and r != 0):
            v = min(l,r)
        elif(l == 0):
            v = r
        elif(r==0):
            v = l
        return 1 + v