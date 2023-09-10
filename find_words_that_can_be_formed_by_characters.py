import pytest


class Solution:
    @staticmethod
    def is_entering(word: str, chars: str):
        for letter in word:
            if letter not in chars:
                return False
            chars = chars.replace(letter, '', 1)
        return True

    def countCharacters(self, words: list[str], chars: str) -> int:
        return sum(len(word) for word in words if self.is_entering(word, chars))


@pytest.mark.parametrize('words, chars, expected_result', [
    (["cat", "bt", "hat", "tree"], "atach", 6),
    (["hello", "world", "leetcode"], "welldonehoneyr", 10)
])
def test_solution(words, chars, expected_result):
    sol = Solution()
    assert sol.countCharacters(words, chars) == expected_result
