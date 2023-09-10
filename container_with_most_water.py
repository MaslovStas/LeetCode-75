import pytest


class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_height = max_area = 0
        left, right = 0, len(height) - 1

        while left != right:
            cur_height = min(height[left], height[right])
            if cur_height > max_height:
                max_height = cur_height
                max_area = max(cur_height * (right - left), max_area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area


@pytest.mark.parametrize('nums, expected_res', [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1)
])
def test_solution(nums, expected_res):
    sol = Solution()
    assert sol.maxArea(nums) == expected_res
