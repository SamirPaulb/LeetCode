class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        N = len(s)
        ans = ""
        position = 0
        while position < N:
            nx = s[position : position + k]
            ans = ans + nx[::-1] + s[position + k : position + 2 * k]
            position += 2 * k
        return ans

    # def reverseStr(self, s: str, k: int) -> str:
    #     s = list(s)
    #     for i in range(0, len(s), 2*k):
    #         s[i:i+k] = reversed(s[i:i+k])
    #     return "".join(s)

        

s1 = Solution()
s="abcdefg"
k=2
print(s1.reverseStr(s,k))
