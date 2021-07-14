class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        index_c = []
        for i in range(len(s)):
            if s[i] == c:
                index_c.append(i)
        print(index_c)
        ans = []
        for i in range(len(s)):
            a = 2**31
            for j in index_c:
                a = min(a, abs(j-i))
            ans.append(a)
        return ans