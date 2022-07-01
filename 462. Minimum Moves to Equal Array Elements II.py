import unittest
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        mid = nums[(len(nums) - 1) // 2]
        return sum(abs(n - mid) for n in nums)


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [[1, 0, 0, 8, 6], 14]
        ]
        for ci, co in cases:
            result = Solution().minMoves2(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
