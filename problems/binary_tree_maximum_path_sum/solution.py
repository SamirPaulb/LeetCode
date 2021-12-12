# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return
        self.ans = root.val 
        def pathSum(root):
            if not root: return 0
            maxLeft = pathSum(root.left)
            maxRight = pathSum(root.right)
            
            strightSum = max(root.val + max(maxLeft, maxRight), root.val)
            maxSum = max(strightSum, maxLeft + root.val + maxRight)
            self.ans = max(self.ans, maxSum)
            
            return strightSum
        
        pathSum(root)
        return self.ans