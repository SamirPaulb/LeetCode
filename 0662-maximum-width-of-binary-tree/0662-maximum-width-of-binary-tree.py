# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root: return res
        q = collections.deque()
        q.append((root, 0))
        while q:
            n = len(q)
            res = max(res, q[-1][1] - q[0][1] + 1)
            for _ in range(n):
                node, dist = q.popleft()
                if node.left: q.append((node.left, 2*dist-1))
                if node.right: q.append((node.right, 2*dist))
        
        return res