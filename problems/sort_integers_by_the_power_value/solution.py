class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def power(x):
            count = 0
            while x != 1:
                if x%2 == 0:
                    x = x / 2
                else:
                    x = 3 * x + 1
                count += 1
            return count
        
        d = {}
        for i in range(lo, hi+1):
            d[i] = power(i)
        
        key = list(d.keys())
        value = list(d.values())
        
        a = []
        for i in value:
            a.append(i)
        a.sort()
        
        for i in range(k-1):
            if a[0] == a[1]:
                key.pop(value.index(a[0]))
                value.pop(value.index(a[0]))
                a.pop(0)
            else:
                a.pop(0)
        
        return key[value.index(a[0])]              
            