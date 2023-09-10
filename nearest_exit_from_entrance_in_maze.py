from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m, n = len(maze), len(maze[0])
        d = deque()
        d.append((*entrance, 0))
        maze[entrance[0]][entrance[1]] = '+'

        while d:
            row, col, deep = d.popleft()

            if (row in (0, m - 1) or col in (0, n - 1)) and [row, col] != entrance:
                return deep

            for drow, dcol in (-1, 0), (0, -1), (0, 1), (1, 0):
                new_row, new_col = row + drow, col + dcol

                if 0 <= new_row < m and 0 <= new_col < n and maze[new_row][new_col] == '.':
                    d.append((new_row, new_col, deep + 1))
                    maze[new_row][new_col] = '+'

        return -1


maze = [['+', '+', '+', '+'],
        ["+", ".", ".", "+"],
        [".", ".", ".", "+"],
        ["+", "+", "+", "."]]
entrance = [2, 2]
sol = Solution()
print(sol.nearestExit(maze, entrance))
