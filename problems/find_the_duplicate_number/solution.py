class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        numberLine = [0 for i in range(10**5 + 1)]
        
        for i in nums:
            numberLine[i] += 1
        
        for i in range(len(numberLine)):
            if numberLine[i] > 1:
                return i
        