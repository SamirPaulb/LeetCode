'''
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
'''

class Solution:
    def __init__(self):
        self.arr = []
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        self.arr.append(root.val)
        for i in range(len(root.children)):
            self.preorder(root.children[i])
        return self.arr