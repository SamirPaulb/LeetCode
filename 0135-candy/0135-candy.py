class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = max(1+candy[i-1], candy[i])
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(1+candy[i+1], candy[i])
        
        return sum(candy)