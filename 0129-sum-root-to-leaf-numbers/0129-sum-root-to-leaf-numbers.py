# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def preorder(root, path):
            if not root: return 0
            if not root.left and not root.right:
                self.res += int(path + str(root.val))
                return
            preorder(root.left, path + str(root.val))
            preorder(root.right, path + str(root.val))
        
        preorder(root, "")
        return self.res
        