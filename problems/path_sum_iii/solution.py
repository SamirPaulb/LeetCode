# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def incluideCurrNode(node, targetSum, res):
            res = 0
            if not node: return 0
            if node.val == targetSum: res += 1
            res += incluideCurrNode(node.left, targetSum - node.val, res)
            res += incluideCurrNode(node.right, targetSum - node.val, res)
            return res
                    
        if not root: return 0
        return self.pathSum(root.left, targetSum) + incluideCurrNode(root, targetSum, 0) + self.pathSum(root.right, targetSum)