import unittest


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append((c, i))
            else:
                if stack and stack[-1][0] == '(':
                    stack.pop()
                    if stack:
                        last, lastIdx = stack[-1]
                        ans = max(ans, i - lastIdx)
                    else:
                        ans = max(ans, i + 1)
                else:
                    stack.append((c, i))

        return ans


class Test(unittest.TestCase):
    def test(self):
        cases = [
            ["(()", 2],
            [")()())", 4],
            ["", 0],
            ["()", 2],
        ]
        for ci, co in cases:
            result = Solution().longestValidParentheses(ci)
            assert result == co, (ci, co, result)
        # cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
    unittest.main(exit=False)
