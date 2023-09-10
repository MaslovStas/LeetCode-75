from collections import defaultdict


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = [False] * n

        def dfs(city):
            for neighbor in graph[city]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        provinces = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                provinces += 1
                dfs(i)

        return provinces


sol = Solution()
print(sol.findCircleNum([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]))
