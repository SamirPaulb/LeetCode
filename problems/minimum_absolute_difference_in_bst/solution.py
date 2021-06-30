# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.a = []
        
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(root):
            if root.left:
                inorder(root.left)
            self.a.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        m = abs(self.a[1] - self.a[0])
        for i in range(len(self.a)-1):       # only aplicable for SORTED ARRAY  and as in Inorder method the array is already sorted
            if abs(self.a[i+1] - self.a[i]) < m:
                m = self.a[i+1] - self.a[i] 
        return m
    