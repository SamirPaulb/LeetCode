# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def sym(l, r):
            if not l and not r: return True
            elif not l or not r: return False
            return l.val == r.val and sym(l.left, r.right) and sym(l.right, r.left)
        
        return sym(root.left, root.right)
            
        
        