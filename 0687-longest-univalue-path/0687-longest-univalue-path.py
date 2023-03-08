class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def solve(root):
            if not root: return 0
            if not root.left and not root.right: return 0
            tmp = 0
            l = solve(root.left)
            if root.left and root.val == root.left.val:
                tmp = max(tmp, 1 + l)
            r = solve(root.right)
            if root.right and root.val == root.right.val:
                tmp = max(tmp, 1 + r)
            self.res = max(self.res, tmp)
            if root.left and root.right and root.val == root.left.val == root.right.val:
                self.res = max(self.res, 2 + l + r)
            return tmp
        
        solve(root)
        return self.res
            