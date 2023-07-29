class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.dct = {}

    def insert(self, val: int) -> bool:
        if val in self.dct: return False
        i = len(self.arr)
        self.dct[val] = i
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dct: return False
        i = self.dct[val]
        last = self.arr[-1]
        self.dct[last] = i
        self.arr[i], self.arr[-1] = self.arr[-1], self.arr[i]
        self.arr.pop()
        del self.dct[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
