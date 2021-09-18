# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        cur = root
        while True:
            if cur != None:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                ans.append(cur.val)
                cur = cur.right
            else:
                break
        return ans