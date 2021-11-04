class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def longPath(root):
            if not root: return 0
            lMax = longPath(root.left)
            rMax = longPath(root.right)
            
            if root.left:
                if root.val == root.left.val: lMax += 1
                else: lMax = 0
            if root.right: 
                if root.val == root.right.val: rMax += 1
                else: rMax = 0
            
            self.result = max(self.result, lMax + rMax)
            return max(lMax, rMax)
        
        longPath(root)
        
        return self.result
        
        