class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.res = root.val
        def solve(root):
            if not root: return 0 
            
            l = solve(root.left)
            r = solve(root.right)
            
            temp = max(root.val + max(l, r), root.val)
            ans = max(temp, root.val + l + r)
            self.res = max(self.res, ans)
            
            return temp
        
        solve(root)
        return self.res
    