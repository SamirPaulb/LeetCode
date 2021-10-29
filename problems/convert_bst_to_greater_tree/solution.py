class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.s = 0
        
        def right_root_left_order(root):
            if not root: return
            if root.right:
                right_root_left_order(root.right)
            self.s += root.val
            root.val = self.s
            if root.left:
                right_root_left_order(root.left)
        
        right_root_left_order(root)
        
        return root
                       
                       