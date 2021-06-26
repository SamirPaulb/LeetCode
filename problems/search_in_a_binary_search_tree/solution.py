# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return
        else:
            if root.val < val:
                root  = self.searchBST(root.right, val)
            elif root.val> val:
                root = self.searchBST( root.left, val)
        return root
        