import unittest

# Monotonic Stack
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rst = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev = stack.pop()
                rst[prev] = i - prev
            stack.append(i)
        return rst


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [[73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]],
            [[30, 40, 50, 60], [1, 1, 1, 0]],
            [[30, 60, 90], [1, 1, 0]],
        ]
        for ci, co in cases:
            result = Solution().dailyTemperatures(ci)
            assert result == co, (ci, co, result)
        # cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
    unittest.main(exit=False)
