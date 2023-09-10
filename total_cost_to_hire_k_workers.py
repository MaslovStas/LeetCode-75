import heapq
from collections import deque


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        left, right = costs[:candidates], costs[max(candidates, len(costs) - candidates):]
        heapq.heapify(left)
        heapq.heapify(right)
        d = deque(costs[candidates: -candidates])
        res = 0
        for _ in range(k):
            if not right or left and left[0] <= right[0]:
                worker = heapq.heappop(left)
                if d:
                    heapq.heappush(left, d.popleft())
            else:
                worker = heapq.heappop(right)
                if d:
                    heapq.heappush(right, d.pop())
            res += worker

        return res


print(Solution().totalCost(costs=
                           [31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58], k=11, candidates=2))
