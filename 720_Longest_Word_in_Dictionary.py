class Solution(object):
    # def longestWord(self, words):
    #     words.sort()
    #     words_set, longest_word = set(['']), ''
    #     for word in words:
    #         if word[:-1] in words_set:
    #             words_set.add(word)
    #             if len(word) > len(longest_word):
    #                 longest_word = word
    #     return longest_word

    # def longestWord(self, words):
    #     ans = ""
    #     wordset = set(words)
    #     for word in words:
    #         if len(word) > len(ans) or len(word) == len(ans) and word < ans:
    #             if all(word[:k] in wordset for k in xrange(1, len(word))):
    #                 ans = word
    #     return ans

    def longestWord(self, words):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True
        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i
        stack = trie.values()
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])
        return ans
