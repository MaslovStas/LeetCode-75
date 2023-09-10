class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        buy, sell = -prices[0], 0
        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)
        return sell


print(Solution().maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
