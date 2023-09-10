class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
for p in (1, 2, 3, 9, 4, 7):
    param_1 = obj.next(p)
    print(param_1)
