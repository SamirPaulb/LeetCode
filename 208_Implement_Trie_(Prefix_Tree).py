class TrieNode(object):
    # https://leetcode.com/articles/implement-trie-prefix-tree/#trie-node-structure
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.links = [None] * 26
        self.isEnd = False

    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] != None

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def setEnd(self):
        self.isEnd = True


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in range(len(word)):
            ch = word[i]
            if node.containsKey(ch) is False:
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.setEnd()

    def searchPrefix(self, word):
        node = self.root
        for i in range(len(word)):
            ch = word[i]
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return None
        return node


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.searchPrefix(word)
        return node is not None and node.isEnd


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.searchPrefix(prefix)
        return node is not None


        # Your Trie object will be instantiated and called as such:
        # trie = Trie()
        # trie.insert("somestring")
        # trie.search("key")