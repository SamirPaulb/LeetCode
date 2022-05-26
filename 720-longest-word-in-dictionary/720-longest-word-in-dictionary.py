class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.val = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        cur.val = word
    
    def bfs(self):
        q = [self.root]
        res = ''
        while q:
            cur = q.pop(0)
            for child in cur.children.values():
                if child.endOfWord:
                    q.append(child)
                    if len(child.val) > len(res):
                        res = child.val
        return res
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        return trie.bfs()