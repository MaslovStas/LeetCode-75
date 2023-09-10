from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        q = deque()
        oranges = rotten = 0
        for i, row in enumerate(grid):
            for j in range(len(row)):
                orange = grid[i][j]
                oranges += bool(orange)
                if orange == 2:
                    rotten += 1
                    q.append((i, j, 0))

        deep = 0
        while q:
            row, col, deep = q.popleft()
            for drow, dcol in ((-1, 0,), (0, -1), (0, 1), (1, 0)):
                new_row, new_col = row + drow, col + dcol
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    q.append((new_row, new_col, deep + 1))
                    rotten += 1

        return deep if oranges == rotten else -1


grid = [[2, 1, 1],
        [1, 1, 0],
        [0, 1, 2]]
sol = Solution()
print(sol.orangesRotting(grid))
