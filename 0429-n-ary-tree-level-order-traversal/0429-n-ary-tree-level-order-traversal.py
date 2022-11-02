"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            n = len(q)
            tmp = []
            for _ in range(n):
                node = q.popleft()
                tmp.append(node.val)
                for c in node.children:
                    q.append(c)
            res.append(tmp)
        
        return res