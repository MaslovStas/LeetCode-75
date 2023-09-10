class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_ans, cur_nums = '', 0
        for c in s:
            if c == '[':
                stack.append((cur_ans, cur_nums))
                cur_ans, cur_nums = '', 0
            elif c == ']':
                prev_ans, prev_nums = stack.pop()
                cur_ans = prev_ans + prev_nums * cur_ans
            elif c.isdigit():
                cur_nums = cur_nums * 10 + int(c)
            else:
                cur_ans += c
        return cur_ans


sol = Solution()
print(sol.decodeString('a3[b2[c]]r4[d]'))
