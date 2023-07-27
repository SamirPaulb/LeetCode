class MyCalendar:

    def __init__(self):
        self.booking = set()

    def book(self, start: int, end: int) -> bool:
        for s,e in self.booking:
            if start < e and end > s: return False
        self.booking.add((start, end))
        return True