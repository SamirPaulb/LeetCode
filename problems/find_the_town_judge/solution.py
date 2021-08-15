from numpy import *
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = array([[0,0]]*n)
        # 1st element of each sub array is you are trusting to how many people
        # 2nd alement of each subarray is number of people trust on you
        for i in range(len(trust)):
            trust_count[trust[i][0]-1][0] += 1
            trust_count[trust[i][1]-1][1] += 1
        for i in range(len(trust_count)):
            if trust_count[i][0] == 0 and trust_count[i][1] == n-1:
                return i+1
        return -1