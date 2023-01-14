class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.val = "-"

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.val = c
        cur.isWord = True
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        for pd in products:
            self.addWord(pd)
        
        def dfs(cur, arr, tmp):
            if len(arr) == 3 or not cur: return 
            if cur.isWord: 
                arr.append(tmp)
            for child in cur.children.values():
                dfs(child, arr, tmp+child.val)
        
        cur = self.root
        res = []
        for i, c in enumerate(searchWord):
            if c not in cur.children: 
                break
            cur = cur.children[c]
            arr = []
            dfs(cur, arr, "")
            for j in range(len(arr)):
                arr[j] = searchWord[:i+1] + arr[j]
            res.append(arr)
        res += [[] for i in range(len(searchWord) - len(res))]
        
        return res