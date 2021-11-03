class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        p, q = root.left, root.right
        
        def check(p, q):
            if not p and not q: return True
            elif (not p and q) or (p and not q) or (p.val != q.val): return False
            return check(p.left, q.right) and check(p.right, q.left)
        
        return check(p, q)