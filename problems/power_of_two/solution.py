from math import log
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        # Since error exist, can't use float.is_integer() to check
        # So I choose to check it back
        if n <= 0: return False
        res = round(log(n, 2))
        return 2**res == n