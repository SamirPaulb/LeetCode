# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def solve(root):
            if not root: return 0
            l = solve(root.left)
            r = solve(root.right)
            if root.left and root.val == root.left.val:
                l += 1
            else:
                l = 0
            
            if root.right and root.val == root.right.val:
                r += 1
            else:
                r = 0
            
            self.res = max(self.res, l+r)
            return max(l, r)
        
        solve(root)
        return self.res