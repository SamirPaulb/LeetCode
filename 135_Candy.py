class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # https://discuss.leetcode.com/topic/5243/a-simple-solution
        if ratings is None or len(ratings) == 0:
            return 0
        ls = len(ratings)
        num = [1] * ls
        for i in range(1, ls):
            if ratings[i] > ratings[i - 1]:
                num[i] = num[i - 1] + 1
        for i in range(ls - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                num[i - 1] = max(num[i] + 1, num[i - 1])
        return sum(num)

