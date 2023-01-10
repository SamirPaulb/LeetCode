class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        cnt = collections.Counter()
        for w, h in rectangles:
            r = w/h
            cnt[r] += 1
        
        res = 0
        for r in cnt:
            if cnt[r] > 1: res += cnt[r]*(cnt[r]-1)//2
        return res