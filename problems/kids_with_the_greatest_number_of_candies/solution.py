class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        L = []
        for i in range(len(candies)):
            for j in range(0,extraCandies+1):
                if candies[i] + j == m:
                    L.append(True)
                    break
            else:
                L.append(False)
        return L
            