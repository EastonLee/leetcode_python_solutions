import unittest
from typing import List


class Solution:
    def missingNumber2(self, nums: List[int]) -> int:
        n = set(nums)
        for i in range(len(nums) + 1):
            if i not in n:
                return i

    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        x1, x2 = 0, 0
        for i in range(length + 1):
            x1 ^= i
        for i in nums:
            x2 ^= i
        return x1 ^ x2


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [[3, 0, 1], 2],
            [[0, 1], 2],
            [[9, 6, 4, 2, 3, 5, 7, 0, 1], 8]
        ]
        for ci, co in cases:
            result = Solution().missingNumber(ci)
            assert result == co, (ci, co, result)
        # cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
    unittest.main(exit=False)
