class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        min_end = float('-inf')
        count = 0
        for start, end in sorted(intervals, key=lambda x: x[1]):
            if start >= min_end:
                min_end = end
                count += 1
        return len(intervals) - count


print(Solution().eraseOverlapIntervals(intervals=[[0, 2], [1, 3], [1, 3], [2, 4], [3, 5], [3, 5], [4, 6]]))
