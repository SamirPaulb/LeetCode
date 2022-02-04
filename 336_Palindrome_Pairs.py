class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # https://leetcode.com/problems/palindrome-pairs/discuss/79219/Python-solution~
        # reverse word and create a word to index map
        word2index, res = dict([(w[::-1], i) for i, w in enumerate(words)]), []
        for i, word in enumerate(words):
            for j in xrange(len(word) + 1):
                # Use prefix and postfix
                # rather than going through all posible combinations
                prefix, postfix = word[:j], word[j:]
                # prefix + postfix + reverse(prfix)
                if prefix in word2index and i != word2index[prefix] and postfix == postfix[::-1]:
                    res.append([i, word2index[prefix]])
                # reverse(postfix) + prefix + postfix
                if j > 0 and postfix in word2index and i != word2index[postfix] and prefix == prefix[::-1]:
                    res.append([word2index[postfix], i])
        return res
