# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def minDiffInBST(self, root: TreeNode) -> int:
        def inorder(root):
            if root.left:
                inorder(root.left)
            self.arr.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        s = abs(self.arr[1] - self.arr[0])
        for i in range(1,len(self.arr)-1):
            if s > abs(self.arr[i] - self.arr[i+1]):
                s = abs(self.arr[i] - self.arr[i+1])
        return s
        
        