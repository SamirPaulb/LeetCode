class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        @lru_cache()
        def is_parlindrome(w):
            return w == w[::-1]
        
        word2idx = {word:idx for idx, word in enumerate(words)}
        res = []
        for i in range(len(words)):
            word = words[i]
            w_rev = word[::-1]
            for suff_length in range(len(word)+1):
                # word + others
                expected_suffix = word[:suff_length][::-1]
                if expected_suffix in word2idx and word2idx[expected_suffix] != i:
                    # this might be a parlindrome, check the middle part
                    if is_parlindrome(word[suff_length:]):
                        res.append((i, word2idx[expected_suffix]))
                
                if suff_length == len(word): continue # duplication
                # others + word
                expected_suffix = w_rev[:suff_length]
                if expected_suffix in word2idx and word2idx[expected_suffix] != i:
                    # this might be a parlindrome, check the middle part
                    if is_parlindrome(w_rev[suff_length:]):
                        res.append((word2idx[expected_suffix], i))
                
        return res
