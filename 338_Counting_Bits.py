class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            # res[left:last] + last bit
            res[i] = res[i >> 1] + (i & 1)
        return res

