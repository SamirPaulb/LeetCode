class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        elif (not p and q) or (p and not q) or (p.val != q.val): return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    