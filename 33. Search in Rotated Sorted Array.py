import unittest
from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the index of the smallest number
        left, right, smallest = 0, len(nums) - 1, 0
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid

        if nums[left] < nums[right]:
            smallest = left
        else:
            smallest = right

        nums = nums[smallest:] + nums[:smallest]
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid

        if nums[left] == target:
            return (left + smallest) % len(nums)
        if nums[right] == target:
            return (right + smallest) % len(nums)
        return -1


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [dict(nums=[4, 5, 6, 7, 0, 1, 2], target=0), 4],
            [dict(nums=[4, 5, 6, 7, 0, 1, 2], target=3), -1],
            [dict(nums=[1], target=0), -1],
        ]
        for ci, co in cases:
            result = Solution().search(ci['nums'], ci['target'])
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
