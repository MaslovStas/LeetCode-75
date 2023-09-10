class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        symbols = dict(zip(map(str, range(2, 10)), ('abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')))

        res = []

        def backtrack(next_digits: str, combinations: str = '') -> None:
            if not next_digits:
                res.append(combinations)
                return

            for letter in symbols[next_digits[0]]:
                backtrack(next_digits[1:], letter + combinations)

        backtrack(digits)
        return res


sol = Solution()
print(sol.letterCombinations('23'))
