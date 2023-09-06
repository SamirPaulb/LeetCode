# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dist = {}
        q = collections.deque()
        q.append((root, 0))
        l = 0
        while q:
            n = len(q)
            for _ in range(n):
                node, d = q.popleft()
                if d not in dist:
                    dist[d] = []
                dist[d].append((l, node.val))
                if node.left: q.append((node.left, d-1))
                if node.right: q.append((node.right, d+1))
            l += 1
        
        res = []
        keys = sorted(list(dist.keys()))
        for k in keys:
            res.append([v for l,v in sorted(dist[k])])
        return res
        