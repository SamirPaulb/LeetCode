# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        a = []
        def inorder(root):
            if root.left:
                inorder(root.left)
            a.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        
        fa = 0
        la = len(a) - 1
        while fa < la:
            if a[fa] + a[la] > k:
                la -= 1
            elif a[fa] + a[la] < k:
                fa += 1
            else:
                return k == a[fa] + a[la]
                break

        
         
 