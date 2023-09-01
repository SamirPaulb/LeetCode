class trieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False
    

class Trie:

    def __init__(self):
        self.root = trieNode()    

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = trieNode()
            cur = cur.children[w]
        cur.endWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.children: return False
            cur = cur.children[w]
        return cur.endWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w not in cur.children: return False
            cur = cur.children[w]
        return True

