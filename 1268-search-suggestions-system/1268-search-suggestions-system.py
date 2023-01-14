class Node:
    def __init__(self):
        self.val = ""
        self.children = {}
        self.suggestions  = []

class Trie:
    def __init__(self):
        self.root = Node()
    
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
            cur.val = c
            if len(cur.suggestions) < 3:
                cur.suggestions.append(word)
    
    def getSuggestions(self, searchWord):
        cur = self.root
        res = []
        for c in searchWord:
            if c in cur.children:
                cur = cur.children[c]
                res.append(cur.suggestions)
            else: 
                break
        res += [[] for i in range(len(searchWord)-len(res))]
        return res
                

class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        trie = Trie()
        for word in products:
            trie.addWord(word)
        return trie.getSuggestions(searchWord)