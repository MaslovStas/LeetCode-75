from collections import Counter

import pytest


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rows = map(tuple, grid)
        cols = (tuple(row[i] for row in grid) for i in range(len(grid)))
        c1, c2 = Counter(rows), Counter(cols)
        return sum(c1[item] * c2[item] for item in c1 & c2)


@pytest.mark.parametrize('grid, expected_res', [
    ([[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1),
    ([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], 3)
])
def test_solution(grid, expected_res):
    sol = Solution()
    assert sol.equalPairs(grid) == expected_res
