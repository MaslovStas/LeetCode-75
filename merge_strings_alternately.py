import pytest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len_str = min(len(word1), len(word2))
        array = [''] * 2 * min_len_str
        array[::2] = word1[:min_len_str]
        array[1::2] = word2[:min_len_str]
        return ''.join(array) + word1[min_len_str:] + word2[min_len_str:]


@pytest.mark.parametrize('word1, word2, expected_word', [
    ('abc', 'pqr', 'apbqcr'),
    ('ab', 'pqrs', 'apbqrs')
])
def test_solution(word1, word2, expected_word):
    sol = Solution()
    assert sol.mergeAlternately(word1, word2) == expected_word
