class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        if sum(range(9, 9 - k, -1)) < n:
            return []

        max_num = min(n - sum(range(1, k)), 9)
        if max_num < k:
            return []

        res = []

        def backtrack(count: int, start: int = 1, digits: list = None):
            if digits is None:
                digits = []
            if count == 0:
                if sum(digits) == n:
                    res.append(digits)
                return

            for num in range(start, max_num - count + 2):
                backtrack(count - 1, num + 1, digits + [num])

        backtrack(count=k)
        return res


sol = Solution()
print(sol.combinationSum3(k=3, n=15))
