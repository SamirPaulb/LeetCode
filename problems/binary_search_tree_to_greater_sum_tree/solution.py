# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.total = 0
        def dfs(root):
            if not root: return
            dfs(root.right)
            self.total += root.val
            root.val = self.total
            dfs(root.left)
        
        dfs(root)
        return root