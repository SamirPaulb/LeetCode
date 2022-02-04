class Solution(object):
    # def validPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     def is_pali_range(i, j):
    #         return all(s[k] == s[j - k + i] for k in range(i, j))

    #     for i in xrange(len(s) / 2):
    #         if s[i] != s[~i]:
    #             j = len(s) - 1 - i
    #             return is_pali_range(i + 1, j) or is_pali_range(i, j - 1)
    #     return True

    # Actually we can make this solution more general
    def validPalindrome(self, s):
        return self.validPalindromeHelper(s, 0, len(s) - 1, 1)

    def validPalindromeHelper(self, s, left, right, budget):
        # Note that budget can be more than 1
        while left < len(s) and right >= 0 and left <= right and s[left] == s[right]:
            left += 1
            right -= 1
        if left >= len(s) or right < 0 or left >= right:
            return True
        if budget == 0:
            return False
        budget -= 1
        return self.validPalindromeHelper(s, left + 1, right, budget) or self.validPalindromeHelper(s, left, right - 1, budget)
