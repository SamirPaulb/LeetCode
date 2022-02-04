class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # let permutations with first identical num be a block
        # target in (k - 1) / (n - 1)! block
        remain = range(1, n + 1)
        if k <= 1:
            return ''.join(str(t) for t in remain)
        total = 1
        for num in remain[:-1]:
            total *= num
        res = self.do_getPermutation(remain, total, n - 1, k - 1)
        return ''.join(str(t) for t in res)


    def do_getPermutation(self, remain, curr, n, k):
        if n == 0 or k <= 0 or curr == 0:
            return remain
        # which block
        step = k / curr
        # remain k value
        k %= curr
        curr /= n
        res = [remain[step]] + self.do_getPermutation(remain[:step] + remain[step + 1:], curr, n - 1, k)
        return res

if __name__ == '__main__':
    s = Solution()
    print s.getPermutation(3, 2)
    # print s.getPermutation(2, 2)