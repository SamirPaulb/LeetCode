# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.s = 0
        
        def inorder(root):
            if root.left:
                inorder(root.left)
            if low < root.val < high:
                self.s += root.val
            if root.right:
                inorder(root.right)
        inorder(root)
        return (self.s + low + high)
    