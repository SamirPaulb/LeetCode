import collections


class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        counter = collections.Counter(A)
        return counter.most_common(1)[0][0]


if __name__ == '__main__':
    s = Solution()
    print s.repeatedNTimes([1, 2, 3, 3])
    print s.repeatedNTimes([2, 1, 2, 5, 3, 2])
    print s.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4])
