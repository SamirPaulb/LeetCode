# https://www.youtube.com/watch?v=TO5zsKtc1Ic
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = float("-inf")
        
        def maxPath_util(root):
            if not root: return 0
            leftMax = maxPath_util(root.left)
            rightMax = maxPath_util(root.right)
            
            max_stright = max(root.val + max(leftMax, rightMax), root.val)
            max_case_LR = max(max_stright, leftMax + root.val + rightMax)
            self.result = max(self.result, max_case_LR)
            return max_stright
        
        maxPath_util(root)
        
        return self.result
    