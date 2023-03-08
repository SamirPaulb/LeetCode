class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        left = pairs[0]
        res = 1
        for i in range(1, len(pairs)):
            if left[1] < pairs[i][0]:
                left = pairs[i]
                res += 1
            elif left[1] > pairs[i][1]:
                left = pairs[i]
        
        return res