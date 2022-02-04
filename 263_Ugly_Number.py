class Solution(object):
    # def isUgly(self, num):
    #     """
    #     :type num: int
    #     :rtype: bool
    #     """
    #     if num <= 0:
    #         return False
    #     if num <= 6:
    #         return True
    #     while num % 2 == 0:
    #         num //= 2
    #     while num % 3 == 0:
    #         num //= 3
    #     while num % 5 == 0:
    #         num //= 5
    #     if num == 1:
    #         return True
    #     return False
    def isUgly(self, num):
        if num <= 0:
            return False
        divisors = [2, 3, 5]
        for d in divisors:
            while num % d == 0:
                num /= d
        return num == 1

if __name__ == '__main__':
    s = Solution()
    print s.isUgly(-2147483648)
