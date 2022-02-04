class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        last = [1]
        res = [1]
        for r in range(1, rowIndex + 1):
            res = [1]
            for index in range(len(last) - 1):
                res.append(last[index] + last[index + 1])
            res.append(1)
            last = res
        return res

if __name__ == "__main__":
    s = Solution()
    print s.getRow(3)