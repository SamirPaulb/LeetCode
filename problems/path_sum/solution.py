class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        arr = []
        def solve(root, s): 
            if not root: return s
            if not root.left and not root.right:
                s += root.val
                arr.append(s)
            solve(root.left, s + root.val)
            solve(root.right, s + root.val)
        
        solve(root, 0)
        return targetSum in arr
            