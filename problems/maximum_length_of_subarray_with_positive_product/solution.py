class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        neg = 0
        zero = 0
        for i in nums:
            if i < 0: neg += 1
            elif i == 0: zero += 1
        if neg % 2 == 0 and zero == 0: return len(nums)
        arr = {}
        for i in range(zero+1):
            arr[i] = []
        j = 0
        for i in nums:
            if i == 0:
                j += 1
                continue
            arr[j].insert(0,i)
        print(arr)
        m = 0
        for s in range(len(arr)):
            n = 0
            for i in range(len(arr[s])):
                if arr[s][i] < 0: n += 1
            if n % 2 == 0: 
                m = max(m, len(arr[s]))
            for i in range(len(arr[s])):
                if arr[s][i] < 0:    
                    m = max(m, len(arr[s])-(i+1))
            for i in range(len(arr[s])-1, -1, -1):
                if arr[s][i] < 0:
                    m = max(m, i)
        
        return m
        
        
        
        
        