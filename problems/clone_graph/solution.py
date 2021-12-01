"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # BFS - QUEUE
        if not node: return None
        # map original nodes to their clones
        d = {node : Node(node.val)}
        q = [node]
        
        while q:
            for i in range(len(q)):
                curNode = q.pop()
                for nei in curNode.neighbors:
                    if nei not in d:
                        # store copy of the neighboring node
                        d[nei] = Node(nei.val)
                        q.append(nei)
                    # connect the node copy at hand to its neighboring nodes (also copies) 
                    d[curNode].neighbors.append(d[nei])
        # return copy of the starting node
        return d[node]