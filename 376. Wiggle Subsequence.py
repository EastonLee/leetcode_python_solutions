import unittest
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return [1, 2][nums[1] != nums[0]]
        increasing = nums[1] - nums[0]
        ans = 1
        for i, n in enumerate(nums[2:]):
            if i == 0 and increasing != 0:
                ans += 1
            if n > nums[i + 1]:
                if increasing <= 0:
                    ans += 1
                    increasing = 1
            if n < nums[i + 1]:
                if increasing >= 0:
                    ans += 1
                    increasing = -1
        return ans


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [[1, 7, 4, 9, 2, 5], 6],
            [[1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7],
            [[1, 2, 3, 4, 5, 6, 7, 8, 9], 2],
            [[1, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2],
            [[0, 0], 1],
            [[0, 0, 0], 1],
        ]
        for ci, co in cases:
            result = Solution().wiggleMaxLength(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
