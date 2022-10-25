import unittest
from typing import *


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i == -1:
            nums.reverse()
            return

        # swap the first number that is larger than nums[i] in nums[i+1:]
        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break

        # reverse nums[i+1:]
        nums[i + 1:] = nums[i + 1:][::-1]


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [[1, 2, 3], [1, 3, 2]],
            [[3, 2, 1], [1, 2, 3]],
        ]
        for ci, co in cases:
            Solution().nextPermutation(ci)
            assert ci == co, (ci, co)


if __name__ == '__main__':
    unittest.main(exit=False)
