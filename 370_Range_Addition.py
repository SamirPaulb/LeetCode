class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        # interval problem
        for t in updates:
            start, end, val = t
            res[start] += val
            if end < length - 1:
                res[end + 1] -= val
        # Cumulative sums
        for i in range(1, length):
            res[i] = res[i] + res[i - 1]
        return res
