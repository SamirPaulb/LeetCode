# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            root.left = None
            self.cur.right = root
            self.cur = root
            inorder(root.right)
        
        ans = self.cur = TreeNode(-1)
        inorder(root)
        return ans.right
    