"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return 
        d = {node : Node(node.val)}
        q = [node]
        while q:
            currNode = q.pop()
            for nei in currNode.neighbors:
                if nei not in d:
                    d[nei] = Node(nei.val)
                    q.append(nei)
                d[currNode].neighbors.append(d[nei])
        
        return d[node]
        