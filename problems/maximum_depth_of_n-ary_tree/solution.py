"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        max = 0
        for i in root.children:
            temp = self.maxDepth(i)
            if temp > max:
                max = temp
            
        return (1 + max)
    