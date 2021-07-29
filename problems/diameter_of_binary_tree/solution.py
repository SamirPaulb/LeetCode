# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.s = 0
        def findmaxlen(root):
            if not root:
                return 0
            l = findmaxlen(root.left)
            r= findmaxlen(root.right)
            if self.s < l + r:
                self.s = l + r
            return 1 + max(l, r)
        findmaxlen(root)
        return self.s