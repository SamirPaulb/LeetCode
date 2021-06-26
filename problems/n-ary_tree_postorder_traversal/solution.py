"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
            self.ans = []
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return
        for i in range(len(root.children)):
            self.postorder(root.children[i])
        self.ans.append(root.val)
        return self.ans