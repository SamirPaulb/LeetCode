class MyCalendarTwo:

    def __init__(self):
        self.booked = set()
        self.overlaps = set()
        
    def book(self, start: int, end: int) -> bool:
        for s,e in self.overlaps:
            if start < e and end > s: return False
        
        for s,e in self.booked:
            if start < e and end > s:
                self.overlaps.add((max(start, s), min(end, e)))
        self.booked.add((start, end))
        return True