class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0
        myDict = {}
        r, l = 0, 0   # r = right pointer;  l = left pointer
        maxFrequency = 0   # maximum frequency of the right pointer element
        
        for r in range(len(answerKey)):
            if answerKey[r] not in myDict: myDict[answerKey[r]] = 1
            else: myDict[answerKey[r]] += 1
            maxFrequency = max(maxFrequency, myDict[answerKey[r]])
            while r - l + 1 - maxFrequency > k:
                myDict[answerKey[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        
        return ans