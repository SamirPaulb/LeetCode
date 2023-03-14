# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if not root: 
                return 0, 0
            left = solve(root.left)
            right = solve(root.right)
            withRoot = root.val + left[1] + right[1]
            withoutRoot = max(left) + max(right)
            return withRoot, withoutRoot
        
        return max(solve(root))