class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ls = len(s)
        word_ls = len(words[0])
        target_dict = {}
        # create a targe dict for match
        for word in words:
            try:
                target_dict[word] += 1
            except KeyError:
                target_dict[word] = 1
        res = []
        for start in range(ls - word_ls * len(words) + 1):
            curr_dict = target_dict.copy()
            for pos in range(start, start + word_ls * len(words), word_ls):
                curr = s[pos:pos + word_ls]
                try:
                    curr_dict[curr] -= 1
                    # word appears more than target
                    if curr_dict[curr] < 0:
                        break
                except KeyError:
                    # word not in words
                    break
            else:
                # all word in target dict
                res.append(start)
        return res

    # def findSubstring(self, s, words):
    #     # https://leetcode.com/discuss/87745/3-line-python-solution-sorted-hash-112ms
    #     wLen, wtLen, wSet, sortHash, sLen = len(words[0]), len(words[0]) * len(words), set(words), sorted(
    #         [hash(w) for w in words]), len(s)
    #     h = [hash(s[i:i + wLen]) if s[i:i + wLen] in wSet else None for i in xrange(sLen - wLen + 1)]
    #     return [i for i in xrange(sLen - wtLen + 1) if h[i] and sorted(h[i: i + wtLen: wLen]) == sortHash]

if __name__ == '__main__':
    s = Solution()
    # print s.longestValidParentheses(")(((((()())()()))()(()))(")
    print s.findSubstring('wordgoodgoodgoodbestword', ["word", "good", "best", "good"])

    # [6,9,12]




