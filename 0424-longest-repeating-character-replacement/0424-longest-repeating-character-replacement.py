class Solution:
    def characterReplacement(self, s, k):
        maxFreq = 1
        freq = collections.Counter()
        res = 1
        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            maxFreq = max(maxFreq, freq[s[r]])
            cost = (r-l+1) - maxFreq
            if cost <= k:
                res = max(res, r-l+1)
            else:
                freq[s[l]] -= 1
                l += 1
        
        return res