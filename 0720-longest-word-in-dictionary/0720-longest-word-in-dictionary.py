class trieNode:
    def __init__(self):
        self.val = ""
        self.children = {}
        self.endWord = False

class Solution:
    def __init__(self):
        self.root = trieNode()
        self.root.endWord = True
        self.res = ""
    
    def addWord(self, word):
        cur = self.root
        pre = cur.endWord
        for c in word:
            if c not in cur.children:
                if not pre: break
                cur.children[c] = trieNode()
            pre = cur.endWord
            cur = cur.children[c]
        cur.endWord = True
        if pre and len(word) > len(self.res):
            self.res = word

    def longestWord(self, words: List[str]) -> str:
        words.sort()
        for word in words:
            self.addWord(word)
        return self.res