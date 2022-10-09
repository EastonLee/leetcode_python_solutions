import unittest
from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        hours = [l[1] for l in logs]
        hours = [hours[0]] + [h - hours[i - 1] for i, h in enumerate(hours) if i > 0]
        m = max(hours)
        idxs = [i for i, h in enumerate(hours) if h == m]
        return min([logs[i][0] for i in idxs])


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [dict(n=10, logs=[[0, 3], [2, 5], [0, 9], [1, 15]]), 1]
        ]
        for ci, co in cases:
            result = Solution().hardestWorker(ci['n'], ci['logs'])
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
