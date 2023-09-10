import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            if sum(map(lambda x, k=mid: math.ceil(x / k), piles)) > h:
                low = mid + 1
            else:
                high = mid - 1
        return low


sol = Solution()
print(sol.minEatingSpeed([3,6,7,11], 8))
