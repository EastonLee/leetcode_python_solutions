import unittest


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        m = {}
        for i in range(len(s) - k + 1):
            sub = s[i:i + k]
            m[sub] = True
        return len(m) == 2 ** k


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [("00110110", 2), True],
            [("0110", 1), True],
            [("0110", 2), False],

        ]
        for ci, co in cases:
            result = Solution().hasAllCodes(*ci)
            assert result == co, (ci, co, result)
        # cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
    unittest.main(exit=False)
