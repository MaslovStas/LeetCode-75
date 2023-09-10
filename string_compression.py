import pytest


class Solution:
    def compress(self, chars: list[str]) -> int:
        i, n = 0, len(chars)
        s = ''

        while i < n:
            count = 1
            s += chars[i]
            i += 1
            while i < n and s[-1] == chars[i]:
                count += 1
                i += 1
            if count > 1:
                for digit in str(count):
                    s += digit

        chars[:] = s
        return len(chars)


@pytest.mark.parametrize('chars, expected_result', [
    (["a", "a", "b", "b", "c", "c", "c"], 6),
    (["a"], 1),
    (["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], 4)
])
def test_solution(chars, expected_result):
    sol = Solution()
    assert sol.compress(chars) == expected_result
