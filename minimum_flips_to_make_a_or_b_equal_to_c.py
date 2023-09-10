import math


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        if a | b == c:
            return 0

        max_len = int(math.log2(max(a, b, c))) + 1
        flips = 0
        for i in range(max_len):
            flips += not(((a >> i) & 1) | ((b >> i) & 1)) if ((c >> i) & 1) else ((a >> i) & 1) + ((b >> i) & 1)
        return flips


sol = Solution()
print(sol.minFlips(8, 3, 5))
