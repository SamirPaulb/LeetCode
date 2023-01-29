class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]  # added an empty set
        for a in arr:
            if len(set(a)) < len(a): continue
            a = set(a)
            for c in dp:
                if a & c: # intersection of 2 sets is not empty
                    continue 
                dp.append(a | c)  # added union of set a and c
        
        return max(len(a) for a in dp)
                