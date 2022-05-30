import unittest


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1: return 2147483647

        sign = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        shifts = []
        while True:
            shift = 0
            while divisor << shift <= dividend:
                shift += 1
            if shift:
                dividend -= divisor << (shift - 1)
            else:
                break
            shifts.append(shift - 1)
        rst = sum(map(lambda x: 1 << x, shifts))
        return -rst if sign else rst


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [(10, 3), 3],
            [(7, -3), -2],
        ]
        for ci, co in cases:
            result = Solution().divide(*ci)
            assert result == co, (ci, co, result)
        # cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
    unittest.main(exit=False)
