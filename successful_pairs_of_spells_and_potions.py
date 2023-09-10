from math import ceil


class Solution:
    @staticmethod
    def binary_compare(number: int, sorted_arr: list) -> int:
        low, high = 0, len(sorted_arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if sorted_arr[mid] >= number:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort(reverse=True)
        return [self.binary_compare(ceil(success / spell), potions) for spell in spells]


spells = [3, 1, 2]
potions = [8, 5, 8]
success = 16
sol = Solution()
print(sol.successfulPairs(spells, potions, success))
