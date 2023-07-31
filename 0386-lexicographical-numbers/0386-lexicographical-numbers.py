class Node:
    def __init__(self):
        self.children = {}
        self.val = 0

class Solution:
    def __init__(self):
        self.root = Node()
    
    def addNode(self, s):
        cur = self.root
        for c in s:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.val = int(s)

    def lexicalOrder(self, n: int) -> List[int]:
        for i in range(1, n+1):
            self.addNode(str(i))
        res = []
        def dfs(root):
            for c in root.children:
                node = root.children[c]
                res.append(node.val)
                dfs(node)
        dfs(self.root)
        return res






