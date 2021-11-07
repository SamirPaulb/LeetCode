class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def makeFlate(root):
            if not root: return
            makeFlate(root.left)
            tmp = root.right
            root.right = root.left
            root.left = None
            while root.right:
                root = root.right
            root.right = tmp
            makeFlate(root.right)
        
        makeFlate(root)
        
        return root
        