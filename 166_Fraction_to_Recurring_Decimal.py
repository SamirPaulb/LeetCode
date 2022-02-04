class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'
        fraction = ''
        if (numerator < 0) ^ (denominator < 0):
            fraction += '-'
        dividend = abs(numerator)
        divisor = abs(denominator)
        fraction += str(dividend / divisor)
        remainder = dividend % divisor
        if remainder == 0:
            return fraction
        fraction += '.'
        dic = {}
        while remainder != 0:
            if remainder in dic:
                fraction = fraction[:dic[remainder]] + '(' + fraction[dic[remainder]:] + ')'
                break
            dic[remainder] = len(fraction)
            remainder *= 10
            fraction += str(remainder / divisor)
            remainder %= divisor
        return fraction


if __name__ == '__main__':
    s = Solution()
    # print s.longestValidParentheses(")(((((()())()()))()(()))(")
    print s.fractionToDecimal(-50, 8)
