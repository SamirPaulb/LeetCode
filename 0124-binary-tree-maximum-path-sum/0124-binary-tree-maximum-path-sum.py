# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 
        self.res = -2**31
        def dfs(root):
            if not root: return -2**31
            l = dfs(root.left)
            r = dfs(root.right)
            tmp = max(root.val, root.val + max(l, r))
            self.res = max(self.res, tmp, root.val + l + r)
            return tmp
        
        dfs(root)
        return self.res