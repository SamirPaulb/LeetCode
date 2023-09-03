class StockSpanner:

    def __init__(self):
        self.cnt = {}
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1] <= price:
            res += self.cnt[self.stack.pop()]
        self.stack.append(price)
        self.cnt[price] = res
        return res

