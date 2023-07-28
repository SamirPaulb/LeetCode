class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = collections.Counter()
        for i in answers:
            cnt[i] += 1
        
        res = 0
        for i in cnt:
            c = cnt[i]
            res += ceil(c/(i+1)) * (i+1)
        
        return res