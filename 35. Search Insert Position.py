import unittest
from typing import *


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid

        if nums[left] >= target:
            return left
        if nums[right] >= target:
            return right
        return right + 1


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [dict(nums=[1, 3, 5, 6], target=5), 2],
            [dict(nums=[1, 3, 5, 6], target=2), 1],
            [dict(nums=[1, 3, 5, 6], target=7), 4],
        ]
        for ci, co in cases:
            result = Solution().searchInsert(ci['nums'], ci['target'])
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
