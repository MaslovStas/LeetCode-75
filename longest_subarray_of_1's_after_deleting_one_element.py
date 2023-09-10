import pytest


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n: int = len(nums)
        left: int = 0
        max_length: int = 0
        zeros: int = 0
        for right in range(n):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            cur_length: int = right - left + 1 - zeros
            max_length = max(max_length, cur_length)
        return max_length if max_length < n else max_length - 1


@pytest.mark.parametrize('nums, expected_res', [
    ([1, 1, 0, 1], 3),
    ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
    ([0], 0),
    ([1, 1, 1], 2),
    ([1], 0)
])
def test_solution(nums, expected_res):
    sol = Solution()
    assert sol.longestSubarray(nums) == expected_res
