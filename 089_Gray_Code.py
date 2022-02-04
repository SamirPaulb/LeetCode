class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # https://leetcode.com/discuss/86617/6-line-java-solution-very-concise
        res = [0]
        for i in range(n):
            for j in reversed(range(len(res))):
                res.append(res[j] + (1 << i))
        return res


    # def count_one(self, num):
    #     count = 0
    #     while num:
    #         num &= (num - 1)
    #         count += 1
    #     return count

if __name__ == "__main__":
    s = Solution()
    print s.grayCode(2)

