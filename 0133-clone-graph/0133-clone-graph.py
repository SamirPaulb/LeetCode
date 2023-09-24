"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return
        newNodeDict = {}
        def solve(node):
            if not node: return
            if node not in newNodeDict:
                newNodeDict[node] = Node(node.val)
            for nei in node.neighbors:
                if nei and nei not in newNodeDict:
                    newNodeDict[nei] = Node(nei.val)
                    solve(nei)
                newNodeDict[node].neighbors.append(newNodeDict[nei])
            return node
        
        solve(node)
        return newNodeDict[node]

        