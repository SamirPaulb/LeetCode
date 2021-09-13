# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(l, r):
            if l == None and r == None: return True
            elif l != None and r == None: return False
            elif l == None and r != None: return False
            elif l.val != r.val: return False
            return check(l.left, r.right) and check(l.right, r.left)
        return check(root.left, root.right)
    