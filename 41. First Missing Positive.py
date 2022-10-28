import unittest
from typing import *


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nExists = False
        for i, n in enumerate(nums):
            if n < 0 or n >= len(nums):
                nums[i] = 0
            if n == len(nums):
                nExists = True
        for i, n in enumerate(nums):
            nums[n % (len(nums))] += len(nums)
        for i, n in enumerate(nums):
            if i > 0 and n < len(nums):
                return i
        if not nExists:
            return len(nums)
        return len(nums) + 1


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [[1, 2, 0], 3],
            [[3, 4, -1, 1], 2],
            [[7, 8, 9, 11, 12], 1],
        ]
        for ci, co in cases:
            result = Solution().firstMissingPositive(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
