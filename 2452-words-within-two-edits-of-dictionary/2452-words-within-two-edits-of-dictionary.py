class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for q in queries:
            for d in dictionary:
                count = 0
                for i, j in zip(q, d):
                    if i != j:
                        count += 1
                if count <= 2:
                    res.append(q)
                    break
        
        return res