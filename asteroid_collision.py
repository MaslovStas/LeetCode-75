class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack: list = []
        i = len(asteroids) - 1
        while i >= 0:
            a1 = asteroids[i]
            if not stack:
                stack.append(a1)
                i -= 1
            else:
                a2 = stack[-1]
                if a1 * a2 > 0 or a1 < 0 < a2:
                    stack.append(a1)
                    i -= 1
                elif a1 + a2 == 0:
                    stack.pop()
                    i -= 1
                elif a1 + a2 > 0:
                    stack.pop()
                else:
                    i -= 1
        return stack[::-1]


sol = Solution()
print(sol.asteroidCollision([10, 2, -5]))