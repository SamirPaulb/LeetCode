class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # https://leetcode.com/problems/license-key-formatting/discuss/96497/Python-solution
        S = S.upper().replace('-', '')
        ls = len(S)
        if ls % K == 0:
            pos = K
        else:
            pos = ls % K
        res = S[:pos]
        while pos < ls:
            res += '-' + S[pos:pos + K]
            pos += K
        return res
