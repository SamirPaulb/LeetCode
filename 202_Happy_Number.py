class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # set to store numbers already seen to detect loops
        seen_numbers = set()
        # loop continues until n becomes 1 or a loop is found
        while n > 1 and n not in seen_numbers:
            # store current number to check if it repeats later
            seen_numbers.add(n)
            # replaces n with the sum of squares of its digits
            n = sum(map(lambda x: int(x) * int(x), list(str(n))))
        # if n becomes 1, it's a happy number
        return n == 1
