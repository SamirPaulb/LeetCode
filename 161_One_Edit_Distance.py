class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls_s, ls_t = len(s) ,len(t)
        # reverse to reduce conditions
        if ls_s > ls_t:
            return self.isOneEditDistance(t, s)
        # edit distance is greater than 1
        if ls_t - ls_s > 1:
            return False
        i, shift = 0, ls_t - ls_s
        # find the different position
        while i < ls_s and s[i] == t[i]:
            i += 1
        if i == ls_s:
            return shift > 0
        if shift == 0:
            i += 1
        while i < ls_s and s[i] == t[i + shift]:
            i += 1
        return i == ls_s