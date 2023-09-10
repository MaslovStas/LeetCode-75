from collections import defaultdict
from pprint import pprint


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        graph = defaultdict(list)
        for begin, end in connections:
            graph[begin].append((end, 1))
            graph[end].append((begin, 0))

        visited, stack, count = set(), [0], 0
        while stack:
            city = stack.pop()
            visited.add(city)
            for neighbor, way in graph[city]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    count += way
        return count


sol = Solution()
pprint(sol.minReorder(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]]))
