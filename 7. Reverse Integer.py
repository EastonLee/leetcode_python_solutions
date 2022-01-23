import unittest

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = [1,-1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31) <= rst <= 2**31-1 else 0

class Test(unittest.TestCase):

    def test(self):
        cases = [
            [1534236469, 0],
            [-8463847412, -2147483648]
        ]
        for ci, co in cases:
            print(Solution().reverse(ci))
            assert Solution().reverse(ci) == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main(exit=False)