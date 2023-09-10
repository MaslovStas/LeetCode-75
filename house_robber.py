class Solution:
    def rob(self, nums: list[int]) -> int:
        for i in range(2, len(nums)):
            # print(i, '->', nums[max(i - 3, 0):i-1], nums)
            nums[i] += max(nums[max(i - 3, 0):i - 1])
        return nums


sol = Solution()
print(sol.rob([2, 1, 1, 2]))
