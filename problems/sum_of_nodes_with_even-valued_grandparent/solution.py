# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def inorder(root):
            if root == None:
                return
            if root.left:
                if root.val % 2 == 0:
                    if root.left.left:
                        self.res += root.left.left.val
                    if root.left.right:
                        self.res += root.left.right.val
                inorder(root.left)
            if root.right:
                if root.val % 2 == 0:
                    if root.right.left:
                        self.res += root.right.left.val
                    if root.right.right:
                        self.res += root.right.right.val
                inorder(root.right)
        inorder(root)
        return self.res
                