# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.res = 2**31
        self.prev = 2**31
        def solve(root):
            if not root: return 
            solve(root.left)
            self.res = min(self.res, abs(self.prev - root.val))
            self.prev = root.val
            solve(root.right)
            
        solve(root)
        return self.res
        