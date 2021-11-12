class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def includeCurrRoot(root, targetSum):
            if not root: return 0
            res = 0
            if root.val == targetSum: res += 1
            res += includeCurrRoot(root.left, targetSum - root.val)               
            res += includeCurrRoot(root.right, targetSum - root.val)
            return res
        
        if not root: return 0
        return self.pathSum(root.left, targetSum) + includeCurrRoot(root, targetSum) + self.pathSum(root.right, targetSum)