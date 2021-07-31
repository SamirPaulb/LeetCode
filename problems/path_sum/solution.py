# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        ans = []
        def path(root,s):
            if not root:
                return
            if root.left == None and root.right == None:
                ans.append(s + root.val)
            if root.left:
                path(root.left, s = s + root.val)
            if root.right:
                path(root.right, s =  s + root.val)
        path(root, 0)
        for i in ans:
            if i == targetSum:
                return True
        return False