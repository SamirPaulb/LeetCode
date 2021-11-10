# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(i, j, n):
            if n <= 0: return None
            root = TreeNode(preorder[i])
            if n == 1: return root
            k = j
            while postorder[k] != preorder[i + 1]:
                k += 1
            l = k - j + 1
            root.left = dfs(i + 1, j, l)
            root.right = dfs(i + l + 1, k + 1, n - l - 1)
            return root
        
        return dfs(0, 0, len(preorder))
        