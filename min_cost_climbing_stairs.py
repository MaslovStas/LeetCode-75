class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        one_step, two_step = cost[:2]
        for i in range(2, len(cost)):
            one_step, two_step = two_step, cost[i] + min(one_step, two_step)
        return min(one_step, two_step)


sol = Solution()
print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
