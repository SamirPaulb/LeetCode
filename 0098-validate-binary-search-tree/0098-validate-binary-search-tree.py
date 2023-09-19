# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(mini, root, maxi):
            if not root: return True
            return mini < root.val < maxi and solve(mini, root.left, root.val) and solve(root.val, root.right, maxi)
        
        return solve(-2**31-1, root, 2**31)