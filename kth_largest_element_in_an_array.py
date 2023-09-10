import random


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        if not nums:
            return
        pivot = random.choice(nums)
        left, mid, right = [], [], []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                mid.append(num)
        length_r, length_m = len(right), len(mid)
        if k <= length_r:
            return self.findKthLargest(right, k)
        if k > len(right) + len(mid):
            return self.findKthLargest(left, k - length_r - length_m)
        return mid[0]


print(Solution().findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
