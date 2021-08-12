class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(l, r, st):
            if l >= r:
                return
            st[l], st[r] = st[r], st[l]
            l += 1
            r -= 1
            helper(l, r, st)
        helper(0, len(s)-1, s)