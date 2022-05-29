import unittest


class Solution:
    def numberOfSteps(self, num: int) -> int:
        b = bin(num)[2:]
        return len(b) + b.count('1') - 1


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [14, 6],
            [8, 4],
            [123, 12]
        ]
        for ci, co in cases:
            result = Solution().numberOfSteps(ci)
            assert result == co, (ci, co, result)
        # cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
    unittest.main(exit=False)
