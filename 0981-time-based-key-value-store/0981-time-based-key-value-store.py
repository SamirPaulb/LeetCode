class TimeMap:
        
    def __init__(self):
        self.dic = {}

    def set(self, key, value, timestamp):
        if key not in self.dic:
            self.dic[key] = [(timestamp, value)]
        else:
            self.dic[key].append((timestamp, value))
        
    def get(self, key, timestamp):
        if key not in self.dic: return ""
        arr = self.dic[key]
        l, r = 0, len(arr)-1
        i = 0
        while l < r:
            mid = (l+r+1)//2
            if timestamp < arr[mid][0]:
                r = mid-1
            else:
                l = mid
                
        return arr[l][1] if timestamp >= arr[l][0] else ""