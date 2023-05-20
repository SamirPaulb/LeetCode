# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def solve(root):
            if not root: return -2**31
            l = solve(root.left)
            r = solve(root.right)
            self.res = max(self.res, l, r, root.val, l+r+root.val, max(l,r)+root.val)
            return max(max(l, r) + root.val, root.val)
        
        solve(root)
        return self.res