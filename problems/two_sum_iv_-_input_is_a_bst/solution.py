# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.a = []
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def inorder(root):
            if root == None:
                return
            if root.left:
                inorder(root.left)
            self.a.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        for i in range(len(self.a)-1):
            for j in range(i+1, len(self.a)):
                if self.a[i] + self.a[j] == k:
                    return True
        return False
    