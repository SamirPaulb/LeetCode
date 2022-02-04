class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        # https://leetcode.com/problems/poor-pigs/discuss/94266/Another-explanation-and-solution
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs
