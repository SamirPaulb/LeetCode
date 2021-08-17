class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        pro = 1
        for i in list(n):
            pro *= int(i)
            
        s = 0
        for i in list(n):
            s += int(i)
        
        return pro - s
        