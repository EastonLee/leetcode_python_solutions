import unittest
from typing import List


class Solution:
    def LIS(self, seq: List[int]):
        min_tails = [0] * len(seq)
        size = 0
        for s in seq:
            l, r = 0, size
            while l != r:
                m = (l + r) // 2
                if min_tails[m] < s:
                    l = m + 1
                else:
                    r = m
            min_tails[l] = s
            size = max(l + 1, size)
        return size

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        e = envelopes
        e = sorted(e, key=lambda x: (x[0], -x[1]))
        heights = list(map(lambda x: x[1], e))
        return self.LIS(heights)


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [[[5, 4], [6, 4], [6, 7], [2, 3]], 3],
            [[[1, 1], [1, 1], [1, 1]], 1]
        ]
        for ci, co in cases:
            result = Solution().maxEnvelopes(ci)
            assert result == co, (ci, co, result)
        # cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
    unittest.main(exit=False)
