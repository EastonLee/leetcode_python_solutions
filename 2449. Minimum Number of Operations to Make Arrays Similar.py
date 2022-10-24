import unittest
from typing import *

"""
You are given two positive integer arrays nums and target, of the same length.

In one operation, you can choose any two distinct indices i and j where 0 <= i, j < nums.length and:

set nums[i] = nums[i] + 2 and
set nums[j] = nums[j] - 2.
Two arrays are considered to be similar if the frequency of each element is the same.

Return the minimum number of operations required to make nums similar to target. The test cases are generated such that nums can always be similar to target.
"""


# I can't prove it mathematically
# https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/solutions/2734078/c-java-python-sort-odd-and-even-explained/
class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        onums = filter(lambda x: x % 2 == 1, nums)
        otarget = filter(lambda x: x % 2 == 1, target)
        enums = filter(lambda x: x % 2 == 0, nums)
        etarget = filter(lambda x: x % 2 == 0, target)
        return sum(x - y for x, y in zip(sorted(onums), sorted(otarget)) if x > y) // 2 + sum(
            x - y for x, y in zip(sorted(enums), sorted(etarget)) if x > y) // 2


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [dict(nums=[8, 12, 6], target=[2, 14, 10]), 2],
            [dict(nums=[1, 1, 1, 1, 1], target=[1, 1, 1, 1, 1]), 0],
            [dict(nums=[1, 2, 5], target=[4, 1, 3]), 1],
        ]
        for ci, co in cases:
            result = Solution().makeSimilar(ci['nums'], ci['target'])
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
