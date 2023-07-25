class Solution:
    def intToRoman(self, num: int) -> str:
        vs = [(1000, 'M'), (900,'CM'), (500, 'D'), (400,'CD'), (100, 'C'), (90,'XC'), (50, 'L'), (40,'XL'), (10, 'X'), (9,'IX'), (5, 'V'),(4,'IV'), (1, 'I')]
        res = ''
        i = 0
        while num:
            v,s = vs[i]
            if v <= num:
                d = num // v
                num = num % v
                res += d * s
            i += 1
        
        return res