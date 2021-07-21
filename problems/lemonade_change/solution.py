class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        s = []
        for i in bills:
            if i == 5:
                s.append(i)
            elif i == 10:
                if 5 in s:
                    i5 = s.index(5)
                    s[i5] = 0
                    s.append(10)
                else:
                    return False
            elif i == 20:
                if (5 in s ) and (10 in s):
                    i5 = s.index(5)
                    i10 = s.index(10)
                    s[i5] = 0
                    s[i10] = 0
                    s.append(20)
                elif s.count(5) >= 3:
                    i5 = s.index(5)
                    s[i5] = 0
                    i5 = s.index(5)
                    s[i5] = 0
                    i5 = s.index(5)
                    s[i5] = 0
                    s.append(20)

                else:
                    return False
        return True