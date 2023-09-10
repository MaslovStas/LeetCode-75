class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        i, count = 1, 0
        while i < len(flowerbed) - 1:
            if not any(flowerbed[i - 1:i + 2]):
                count += 1
                i += 2
            else:
                i += 1
        return n <= count
