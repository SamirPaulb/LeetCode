class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if not root: 
                return 0, 0  # withRoot, withoutRoot
            if not root.left and not root.right: 
                return root.val, 0
            left = solve(root.left)
            right = solve(root.right)
            return root.val + left[1] + right[1], max(left) + max(right)          
        return max(solve(root))