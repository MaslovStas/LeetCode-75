from collections import defaultdict
from pprint import pprint


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(dict)
        for (var1, var2), val in zip(equations, values):
            graph[var1].update({var2: val})
            graph[var2].update({var1: 1 / val})

        def get_value_equation(root: str, target: str) -> float:
            if root not in graph or target not in graph:
                return float(-1)

            if root == target:
                return float(1)

            stack = [(root, 1)]
            visited = {root}
            while stack:
                curr, cost = stack.pop()
                for nr in graph[curr]:
                    if nr not in visited:
                        new_cost = cost * graph[curr][nr]
                        if nr == target:
                            return new_cost
                        stack.append((nr, new_cost))
                        visited.add(nr)
            return float(-1)

        return [get_value_equation(root, target) for root, target in queries]


equations = [["a", "b"],
             ["b", "c"]]
values = [2.0, 3.0]
queries = [['a', 'c'], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
sol = Solution()
print(sol.calcEquation(equations, values, queries))
