class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = sorted(score, reverse = True)
        d = {}
        d[arr[0]] = "Gold Medal"
        if len(arr) > 1: d[arr[1]] = "Silver Medal"
        if len(arr) > 2: d[arr[2]] = "Bronze Medal"
        i = 4
        for a in arr[3:]:
            d[a] = str(i)
            i += 1
        
        res = []
        for i in score:
            res.append(d[i])
        
        return res