import pytest


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


@pytest.mark.parametrize('nums, expected_result', [
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], False),
    ([2, 1, 5, 0, 4, 6], True),
    ([3, 0, 1, -7, 2], True),
])
def test_solution(nums, expected_result):
    sol = Solution()
    assert sol.increasingTriplet(nums) == expected_result
