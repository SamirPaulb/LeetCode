# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.s = 0
        def leaf(root, isleav):
            if isleav and root.left ==None and root.right == None:
                self.s += root.val
                return
            if root.left != None : leaf(root.left, True)
            if root.right != None : leaf(root.right, False)
        if root == None:
            return 0
        leaf(root, False)
        return self.s
            