class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://discuss.leetcode.com/topic/63299/python-6-lines-bit-by-bit
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            # use a set to remove duplicate
            prefixes = {num >> i for num in nums}
            # if there is x y in prefixes, where x ^ y = answer ^ 1
            answer += any(answer ^ 1 ^ p in prefixes for p in prefixes)
        return answer


if __name__ == '__main__':
    s = Solution()
    s.findMaximumXOR([3, 10, 5, 25, 2, 8])
