class Solution(object):
    # def isAnagram(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     # sort
    #     return sorted(s) == sorted(t)

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # hash
        # https://leetcode.com/articles/valid-anagram/
        if len(s) != len(t):
            return False
        counter = [0] * 26
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
        for num in counter:
            if num != 0:
                return False
        return True