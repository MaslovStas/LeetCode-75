from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        symbol = {'R': "Radiant", 'D': "Dire"}
        queue = deque(senate)
        queue.append('E')
        rs = 0
        while True:
            curr = queue.popleft()
            if curr == 'E':
                if 'D' not in queue or 'R' not in queue:
                    return symbol[queue.pop()]
                queue.append(curr)
            else:
                if curr == 'R' and rs >= 0 or curr == 'D' and rs <= 0:
                    queue.append(curr)
                rs += (curr == 'R' or -1)


sol = Solution()
print(sol.predictPartyVictory('RDD'))
