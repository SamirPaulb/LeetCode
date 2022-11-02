class Solution:
    def findRightInterval(self, intervals):
        indexDict = {}
        start = []
        for i, [s, e] in enumerate(intervals):
            indexDict[s] = i
            start.append(s)
        start.sort()
        
        def getStart(e):
            ans = 2**31
            l = 0; r = len(start)-1
            while l <= r:
                mid = l + (r - l)//2
                cur = start[mid]
                if cur >= e: ans = min(ans, cur)
                if cur > e:
                    r = mid - 1
                elif cur < e:
                    l = mid + 1
                else:
                    return cur
            return ans
        
        res = []
        for s, e in intervals:
            v = getStart(e)
            if v == 2**31: res.append(-1)
            else:
                res.append(indexDict[v])
        
        return res