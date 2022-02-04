class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if len(J) == 0 or len(S) == 0:
            return 0
        j_set = set(J)
        ans = 0
        for c in S:
            if c in j_set:
                ans += 1
        return ans
