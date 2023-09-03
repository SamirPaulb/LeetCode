class trieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root = trieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = trieNode()
            cur = cur.children[c]
        cur.endWord = True

    def search(self, word: str) -> bool:
        q = collections.deque()
        q.append(self.root)
        for i in range(len(word)):
            n = len(q)
            for _ in range(n):
                cur = q.popleft()
                for c in cur.children:
                    if word[i] == '.' or c == word[i]:
                        q.append(cur.children[c])
                        if i == len(word)-1 and cur.children[c].endWord: return True
        return False
