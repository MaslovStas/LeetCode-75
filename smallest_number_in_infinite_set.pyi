from heapq import heappush, heappop


class SmallestInfiniteSet:

    def __init__(self):
        self._q = []
        self._smallest = 1

    def popSmallest(self) -> int:
        if not self._q or self._q[0] > self._smallest:
            self._smallest += 1
            return self._smallest - 1
        return heappop(self._q)

    def addBack(self, num: int) -> None:
        if num not in self._q and num < self._smallest:
            heappush(self._q, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
obj.addBack(2)
obj.addBack(2)
print(obj.popSmallest())
print(obj.popSmallest())
obj.addBack(5)
print(obj.popSmallest())
