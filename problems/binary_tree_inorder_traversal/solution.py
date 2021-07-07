# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        a = []
        def inorder(root):
            if root == None:
                return 
            inorder(root.left)
            a.append(root.val)
            inorder(root.right)
            return a
        inorder(root)
        return a