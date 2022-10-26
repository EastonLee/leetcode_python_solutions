import unittest
from typing import *


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        start, end = -1, -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid

        if nums[left] == target:
            start = left
        elif nums[right] == target:
            start = right

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid

        if nums[right] == target:
            end = right
        elif nums[left] == target:
            end = left

        return [start, end]


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [dict(nums=[5, 7, 7, 8, 8, 10], target=8), [3, 4]],
            [dict(nums=[5, 7, 7, 8, 8, 10], target=6), [-1, -1]],
            [dict(nums=[5, 7, 7, 8, 8, 10], target=5), [0, 0]],
            [dict(nums=[5, 7, 7, 8, 8, 10], target=10), [5, 5]],
            [dict(nums=[], target=0), [-1, -1]],
        ]
        for ci, co in cases:
            result = Solution().searchRange(ci['nums'], ci['target'])
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
