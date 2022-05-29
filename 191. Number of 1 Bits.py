import unittest


class Solution:
    def hammingWeight(self, n: int) -> int:
        rst = 0
        while n // 2 != 0:
            rst += n % 2
            n = n // 2
        return rst + n


class Test(unittest.TestCase):

    def test(self):
        cases = [
            [0, 0],
            [1, 1],
            [2, 1],
            [3, 2],
            [4, 1],
        ]
        for ci, co in cases:
            result = Solution().hammingWeight(ci)
            assert result == co, (ci, co, result)
        # cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
    unittest.main(exit=False)
