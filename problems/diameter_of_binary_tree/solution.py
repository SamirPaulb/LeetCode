# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.s = 0
        def find_len(root):
            if not root: return 0
            l = find_len(root.left)
            r = find_len(root.right)
            self.s = max(self.s, (l+r))
            return 1 + max(l, r)
        find_len(root)
        return self.s