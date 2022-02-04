class Solution:
    # def mySqrt(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     if x == 0:
    #         return 0
    #     low = 0
    #     high = x
    #     last = x
    #     while high >= low:
    #         mid = (low + high) / 2
    #         temp = mid * mid
    #         if temp == x:
    #             return mid
    #         elif temp < x:
    #             low = mid + 1
    #             last = mid
    #         else:
    #             high = mid - 1
    #     return last

    def mySqrt(self, x):
        # sqrt(x) = 2 * sqrt(x / 4) for n % 4 == 0
        # sqrt(x) = 1 + 2 * sqrt(x / 4) for n % 4 != 0
        if x == 0:
            return 0
        if x < 4:
            return 1
        res = 2 * self.mySqrt(x / 4)
        # (res + 1) * (res + 1) >= 0 for avoiding overflow
        if (res + 1) * (res + 1) <= x and (res + 1) * (res + 1) >= 0:
            return res + 1
        return  res