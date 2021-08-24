# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        a = root
        arr = []
        def inorder(root):
            if root.left:
                inorder(root.left)
            arr.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        print(arr)
        def change(root):
            if root.left:
                change(root.left)
            root.val = sum(arr[arr.index(root.val):len(arr)])
            if root.right:
                change(root.right)
        change(root)
        return a