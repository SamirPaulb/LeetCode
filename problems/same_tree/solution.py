class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        elif not p and q or p and not q: return False
        elif not p.left and q.left or p.left and not q.left: return False
        elif not p.right and q.right or p.right and not q.right: return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)