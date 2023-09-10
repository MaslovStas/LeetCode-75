from functools import reduce


class Solution:
    def tribonacci(self, n: int) -> int:
        return reduce(lambda r, _: r + [r[-1] + r[-2] + r[-3]], range(3, n + 1), [0, 1, 1])[n]


sol = Solution()
print(sol.tribonacci(25))
