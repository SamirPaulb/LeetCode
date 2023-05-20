# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        q = collections.deque([root])
        while q:
            n = len(q)
            res.append(q[-1].val)
            for i in range(n):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                    
        return res