# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def solve(root):
            if not root: return 
            if root.val < low:
                root = solve(root.right)
            elif root.val > high:
                root = solve(root.left)
            else:
                root.left = solve(root.left)
                root.right = solve(root.right)
            return root
        
        return solve(root)
        