class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        st.append(s[0])
        for i in range(1, len(s)):
            if len(st) > 0 and st[-1] == s[i]:
                st.pop(-1)
            else:
                st.append(s[i])
                
        ans = ""
        for i in st:
            ans += i
        return ans
    