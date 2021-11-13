class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.ans, self.pre = float("inf"), float("inf")
        def inorder(root):
            if not root: return
            inorder(root.left)
            if self.pre == float("inf"): self.pre = root.val
            else:
                self.ans = min(self.ans, root.val - self.pre)
                self.pre = root.val
            inorder(root.right)
        
        inorder(root)
        return self.ans