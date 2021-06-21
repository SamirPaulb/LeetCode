# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, mi, ma):
            if not node:
                return True
            if mi >= node.val:
                return False
            if ma <= node.val:
                return False
            return helper(node.left, mi, node.val) and helper(node.right, node.val, ma)
        return helper(root, float("-inf"), float("inf"))
    
            