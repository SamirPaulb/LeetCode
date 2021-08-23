# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(p, q):
            
            if p == None and q != None:
                return False
            elif p != None and q == None:
                return False
            elif p == None and q == None:
                return True
            elif p.val != q.val:
                return False
            
            return check(p.left, q.right) and check(p.right, q.left)
        
        if root.left == None and root.right == None:
            return True
        elif root.left == None and root.right != None:
            return False
        elif root.left != None and root.right == None:
            return False
        return check(root.left, root.right)
                