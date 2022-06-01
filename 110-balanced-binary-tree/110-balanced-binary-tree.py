class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        leftHeight = self.calHeight(root.left)
        rightHeight = self.calHeight(root.right)
        
        return abs(leftHeight - rightHeight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    
    def calHeight(self, root):
        if not root: return 0
        return 1 + max(self.calHeight(root.left), self.calHeight(root.right))