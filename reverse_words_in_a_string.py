from functools import reduce
from operator import mul


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        return [reduce(mul, nums[:i] + nums[i + 1:]) for i in range(len(nums))]


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
