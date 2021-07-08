class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            s = str(x)
            s = s[::-1]
            a = int(s)
            if a > 2**31:
                return 0
            return a
        else:
            x = (-1)*x
            s = str(x)
            s = s[::-1]
            a = (-1)*int(s)
            if a < -2**31 +1:
                return 0
            return a
            