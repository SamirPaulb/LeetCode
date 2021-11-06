class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        elif not root1 or not root2:
            return root1 or root2
        else:
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
            
        return root1