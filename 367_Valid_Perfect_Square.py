class Solution(object):
    # def isPerfectSquare(self, num):
    #     """
    #     :type num: int
    #     :rtype: bool
    #     """
    #     i = 1
    #     while num > 0:
    #         num -= i
    #         i += 2
    #     return num == 0

    def isPerfectSquare(self, num):
        low, high = 1, num
        while low <= high:
            mid = (low + high) / 2
            mid_square = mid * mid
            if mid_square == num:
                return True
            elif mid_square < num:
                low = mid + 1
            else:
                high = mid - 1
        return False

    # def isPerfectSquare(self, num):
    #     x = num
    #     while x * x > num:
    #         x = (x + num / x) / 2
    #     return x * x == num
