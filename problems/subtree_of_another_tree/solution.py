# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        def issame(s,t):
            if s == None and t== None:
                return True
            elif s == None or t == None:
                return False
            return s.val == t.val and issame(s.left, t.left) and issame(s.right, t.right)
        if t == None:
            return True
        elif s == None:
            return False
        elif s == None and t != None:
            return False
        return issame(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    
    
    
    
    