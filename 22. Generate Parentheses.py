import unittest
from typing import *


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(s, l, r):
            if l + r == 2 * n:
                ans.append(s)
                return
            if l < n:
                backtrack(s + '(', l + 1, r)
            if r < l:
                backtrack(s + ')', l, r + 1)

        backtrack('', 0, 0)
        return ans


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [3, ["((()))", "(()())", "(())()", "()(())", "()()()"]],
            [1, ["()"]],
        ]
        for ci, co in cases:
            result = Solution().generateParenthesis(ci)
            assert set(result) == set(co), (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
