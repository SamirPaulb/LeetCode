class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        self.res = False
        def dfs(cur, word):
            if not word:
                return True if cur.isWord else False
            elif word[0] in cur.children:
                cur = cur.children[word[0]]
                return dfs(cur, word[1:])
            elif word[0] == '.':
                tmp = False
                for c in cur.children:
                    tmp |= dfs(cur.children[c], word[1:])
                return tmp
            return False
        
        return dfs(self.root, word)