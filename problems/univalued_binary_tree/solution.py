# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root == None:
            return True
        def helper(root, key):
            if root == None:
                return True
            return root.val == key and helper(root.left, key) and helper(root.right, key)
                
        return helper(root, root.val)
        