import pytest


class Solution:
    @staticmethod
    def getNod(a: int, b: int) -> int:
        if a < b:
            a, b = b, a
        while b != 0:
            a, b = b, a % b
        return a

    @staticmethod
    def getDividersFormRange(word: str, limit: int) -> set:
        n = len(word)
        divs = set()
        for i in range(limit):
            if n % (i + 1) == 0:
                pattern = word[:i + 1]
                quantity = n // (i + 1)
                if pattern * quantity == word:
                    divs.add(pattern)
        return divs

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        n = self.getNod(len(str1), len(str2))
        return max((self.getDividersFormRange(str1, n) & self.getDividersFormRange(str2, n)) or [''])


@pytest.mark.parametrize('str1, str2, expected_str', [
    ('ABC', 'ABCABC', 'ABC'),
    ('ABABAB', 'ABAB', 'AB'),
    ('LEET', 'CODE', '')
])
def test_solution(str1, str2, expected_str):
    sol = Solution()
    assert sol.gcdOfStrings(str1, str2) == expected_str

# if __name__ == '__main__':
#     sol = Solution()
#     str1 = "ABCABC"
#     str2 = "ABC"
#     print(sol.gcdOfStrings(str1, str2))
