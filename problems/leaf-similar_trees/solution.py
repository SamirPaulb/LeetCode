# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
            self.a = []
            self.b = []
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def inorder1(root1):
            if root1.left:
                inorder1(root1.left)
            if root1.left == None and root1.right ==None:
                self.a.append(root1.val)
            if root1.right:
                inorder1(root1.right)
        
        def inorder2(root2):
            if root2.left:
                inorder2(root2.left)
            if root2.left == None and root2.right ==None:
                self.b.append(root2.val)
            if root2.right:
                inorder2(root2.right)
        inorder1(root1)
        inorder2(root2)
        return self.a == self.b