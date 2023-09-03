class trieNode:
    def __init__(self):
        self.s = 0
        self.children = {}

class MapSum:

    def __init__(self):
        self.root = trieNode()
        self.keyVal = {}

    def insert(self, key: str, val: int) -> None:
        newVal = val
        if key in self.keyVal:
            newVal -= self.keyVal[key]
        self.keyVal[key] = val
        cur = self.root
        for c in key:
            if c not in cur.children:
                cur.children[c] = trieNode()
            cur = cur.children[c]
            cur.s += newVal
            
    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.children: return 0
            cur = cur.children[c]
        return cur.s


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)