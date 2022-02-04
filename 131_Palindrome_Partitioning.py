class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # https://discuss.leetcode.com/topic/6186/java-backtracking-solution/2
        result = []
        curr = []
        self.recurPartition(result, curr, s, 0)
        return result

    def recurPartition(self, result, curr, s, start):
        if start == len(s):
            result.append(list(curr))
        for i in range(start, len(s)):
            if self.isPalindrome(s, start, i):
                curr.append(s[start:i + 1])
                self.recurPartition(result, curr, s, i + 1)
                curr.pop()

    def isPalindrome(self, s, begin, end):
        while begin < end:
            if s[begin] != s[end]:
                return False
            begin += 1
            end -= 1
        return True