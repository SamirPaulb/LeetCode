class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def solve(root):
            if not root: return
            solve(root.left)
            tmp = root.right
            root.right = root.left
            root.left = None
            while root.right:
                root = root.right
            root.right = tmp
            solve(root.right)
            
        solve(root)
        return root
        