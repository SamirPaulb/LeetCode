class Solution:
    # https://leetcode.com/problems/longest-palindrome/solution/
    # def longestPalindrome(self, s):
    #     ans = 0
    #     for v in collections.Counter(s).itervalues():
    #         ans += v / 2 * 2
    #         if ans % 2 == 0 and v % 2 == 1:
    #             ans += 1
    #     return ans
    def longestPalindrome(self, s):
        ans = 0
        char_map = {}
        for c in s:
            char_map[c] = char_map.get(c, 0) + 1
        for c in char_map.keys():
            if char_map[c] % 2 == 0:
                ans += char_map.pop(c)
            else:
                ans += char_map[c] / 2 * 2
        if len(char_map) != 0:
            ans += 1
        return ans