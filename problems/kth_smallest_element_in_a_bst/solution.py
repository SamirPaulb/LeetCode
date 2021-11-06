class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root or k <= 0: return root
        self.a = k
        self.ans = root.val
        def inorder(root):
            if not root: return
            if self.a <= 0: return root.val
            inorder(root.left)
            self.a -= 1
            if self.a == 0: self.ans = root.val
            inorder(root.right)
        
        inorder(root)
        
        return self.ans

# Time Complexity = O(N)
# Space Complexity = O(1)
        