# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def samir(root, s):
            if not root:
                return
            if not (root.left or root.right):
                res.append( s + str(root.val) )
            if root.left:
                samir(root.left, s + str(root.val) + "->" )
            if root.right:
                samir(root.right, s + str(root.val) + "->" )
        samir(root, "")
        return res