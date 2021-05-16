# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node: return 0
            val = dfs(node.left) + dfs(node.right)
            if val == 0: return 3
            if val < 3: return 0
            self.ans += 1
            return 1
        return self.ans + 1 if dfs(root) > 2 else self.ans
