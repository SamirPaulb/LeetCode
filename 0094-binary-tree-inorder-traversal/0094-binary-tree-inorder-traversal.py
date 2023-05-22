# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                cur = stack.pop()
                res.append(cur.val)
                root = cur.right
            else:
                break
        
        return res
                