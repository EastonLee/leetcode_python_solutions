import unittest


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        return n * 2


class Test(unittest.TestCase):
    def test(self):
        cases = [
            ["1+7-(7+3+3)+6-3+1", -1]
        ]
        for ci, co in cases:
            result = Solution().calculate(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
