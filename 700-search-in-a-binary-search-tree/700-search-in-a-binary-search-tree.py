# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.res = None
        
        def preorder(root, val):
            if not root: return
            if root.val == val: 
                self.res = root
                return
            preorder(root.left, val)
            preorder(root.right, val)
        
        preorder(root, val)
        return self.res