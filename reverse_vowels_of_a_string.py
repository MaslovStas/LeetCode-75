import pytest
import re


class Solution:
    def reverseVowels(self, s: str) -> str:
        pattern = re.compile('(?i)[aieou]')
        vowels = pattern.findall(s)
        return pattern.sub(lambda x: vowels.pop(), s)


@pytest.mark.parametrize('s, expected_result', [
    ('hello', 'holle'),
    ('leetcode', 'leotcede'),
    ('a.', 'a.'),
    ('.a', '.a'),
    ('ai', 'ia'),
    ('aA', 'Aa'),
])
def test_solution(s, expected_result):
    sol = Solution()
    assert sol.reverseVowels(s) == expected_result
