class MyCalendarTwo:
    
    def __init__(self):
        self.dct = {}
    
    def book(self, start: int, end: int) -> bool:
        self.dct[start] = self.dct[start] + 1 if start in self.dct else 1
        self.dct[end] = self.dct[end] - 1 if end in self.dct else -1
        
        arr = sorted(self.dct.keys())
        s = 0
        for i in arr:
            s += self.dct[i]
            
            if s >= 3:
                self.dct[start] -= 1
                self.dct[end] += 1
                return False
            
        return True


