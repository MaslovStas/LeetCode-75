import pytest


class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        i, n = 0, len(arr)
        while i < n - 1:
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 2
            else:
                i += 1


@pytest.mark.parametrize('arr, expected_arr', [
    ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
    ([0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0])
])
def test_solution(arr, expected_arr):
    sol = Solution()
    sol.duplicateZeros(arr)
    assert arr == expected_arr
