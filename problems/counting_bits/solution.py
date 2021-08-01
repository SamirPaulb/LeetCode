class Solution:
    def countBits(self, n: int) -> List[int]:

        ans = []
        for i in range(n+1):
            ans.append(bin(i).count('1'))
        return ans