# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def lh(root):
            c = 1
            while root:
                c += 1
                root = root.left
        def rh(root):
            c = 1
            while root:
                c += 1
                root = root.right
            return c
        if not root: return 0
        lh = lh(root)
        rh = rh(root)
        if lh == rh: return 2**lh - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
        
        