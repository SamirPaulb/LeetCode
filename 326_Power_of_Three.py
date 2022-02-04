class Solution(object):
    # def isPowerOfThree(self, n):
    #     """
    #     :type n: int
    #     :rtype: bool
    #     """
    #     import math
    #     if n <= 0:
    #         return False
    #     # use round to check
    #     log_res = round(math.log(n, 3), 10)
    #     if log_res - int(log_res) > 0:
    #         return False
    #     return True

    def isPowerOfThree(self, n):
        max3pow = 1162261467
        if n <= 0 or n > max3pow:
            return False
        return max3pow % n == 0